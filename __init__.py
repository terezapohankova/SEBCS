# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SEBCS
                                 A QGIS plugin
 Module for calculation of energy balance features and vegetation water stress indices
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-03-06
        copyright            : (C) 2019 by Jakub Brom, University of South Bohemia in Ceske Budejovice, Faculty of Agriculture
        email                : jbrom@zf.jcu.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SEBCS class from file SEBCS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SEBCS import SEBCS
    return SEBCS(iface)