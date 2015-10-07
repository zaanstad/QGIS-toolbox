##[Zaanstad]=group
##input=vector
##output=output vector

from PyQt4.QtCore import *
from qgis.core import *

from processing.tools.vector import VectorWriter

inputLayer = processing.getObject(input)
features = processing.features(inputLayer)
fields = inputLayer.pendingFields().toList()
outputLayer = VectorWriter(output, None, fields, QGis.WKBPoint, inputLayer.crs())

for ft in features:
  geom = ft.geometry()
  meanPoint = geom.interpolate(geom.length() / 2)
  attrs = ft.attributes()

  outFeat = QgsFeature()
  outFeat.setGeometry(meanPoint)
  outFeat.setAttributes(attrs)
  outputLayer.addFeature(outFeat)
