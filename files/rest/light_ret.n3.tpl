@prefix sweet:  <http://sweet.jpl.nasa.gov/> .
@prefix measures:  <http://example.org/lamp/actuators/light/>. # TODO redirect to the last on .
@prefix lookfor:  <http://pending.of/search/> .
@prefix ssn:  <http://www.w3.org/2005/Incubator/ssn/ssnx/ssn#> .
@prefix actuators:  <http://example.org/lamp/actuators/> .
@prefix : <http://example.org/>.


# Light actuator of the adjustable lamp
# sth/lamp/actuators/light

      
actuators:light a ssn:Sensor;
  ssn:observes sweet:Light ; # redundant: madeObservation and observedProperty defined
  ssn:onPlatform :lamp ; # redundant: inverse of attachedSystem
  lookfor:last measures:last .


{% for id in measures %}
actuators:light ssn:madeObservation measures:{{ id }} .
{% endfor %}