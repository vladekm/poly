==============
Fleet database
==============

Entities
========

Vehicle
-------
provides
########
    CRUD_vehicle
    attach_trailer(Trailer)
    detach_trailer(Trailer)
needs
#####
    persistence
    Trailer

Trailer
-------
provides
########
    CRUD_trailer
    get_size
    load(Load)
    dicharge(Load)
needs
#####
    persistence
    Load

Load
----
provides
########
    CRUD_load
needs
#####
    persistence


GeoNode
-------
provides
########
    get_location
needs
#####
    persistence


Trip
----
provides
########
    CRUD_trip
    assign_vehicle(Vehicle)


Leg
---
provides
########
    CRUD_leg
    set_start_point(Geonode)
    get_start_point(Geonode)
    set_end_point(Geonode)
    get_end_point(Geonode)
needs
#####
    Geonode
