library(leaflet)
library(sf)
library(dplyr)
library(rnaturalearth)
library(rnaturalearthdata)

farmacias <- read.csv("farmacias_filtered.csv")

# Obtener los límites de los estados de México usando rnaturalearth
mexico_estados <- ne_states(country = "Mexico", returnclass = "sf")

# Convertir los datos de farmacias a un objeto sf
farmacias_sf <- st_as_sf(farmacias, coords = c("longitud", "latitud"), crs = 4326, agr = "constant")

# Crear el mapa interactivo con clusters de puntos
mapa <- leaflet(farmacias_sf) %>%
  addTiles() %>%
  # Añadir los puntos con la funcionalidad de clusterización
  addCircleMarkers(
    radius = 5,  # Tamaño fijo para los círculos
    color = "blue",
    stroke = FALSE, 
    fillOpacity = 0.6,
    popup = ~paste("Farmacia:", raz_social),
    clusterOptions = markerClusterOptions()  # Habilitar los clusters de puntos
  ) %>%
  addPolygons(data = mexico_estados,  # Añadir los límites de los estados
              fillColor = NA,
              color = "black",
              weight = 1,
              opacity = 0.5,
              fillOpacity = 0)

# Mostrar el mapa interactivo
mapa
