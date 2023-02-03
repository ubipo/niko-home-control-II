# Niko Home Control II Home Assistant Integration

License: [MIT](LICENSE)

This custom component will allow you to integrate you Niko Connected Controller II in Home Assistant.
You can use a touchscreen profile or the Hobby API account.

This integration communicates directly with the controller. You only need internet when activating/renewing the Hobby
API. If you use a touch screen profile, this isn't even needed.

## Acknowledgements

This custom component is a [spin-off of the hard and excellent work by @filipvh](https://github.com/filipvh/hass-nhc2).
Thanks!

A big thanks to Johan and Koen from Niko for their support and providing me with test equipment.

## What works now?

### NHC Access Control Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

This action exposes a button, camera and a lock.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, which represents the Basic State. This is only available for ring-and-come-in guided
  action. It indicates if the ring-and-come-in is enabled or not.
* **Decline Call Applied On All Devices Binary Sensor**, which represents the Decline Call Applied On All Devices state.

### NHC All Off Action

This action is exposed as a button.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, which represents the Basic State of the AllOff.
* **AllOff Active Binary Sensor**, which represents the AllOffActive state. Be aware that this state is only updated as
  the button is pressed, not when all devices are off.

### NHC Audio Control Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

This action is exposed as media player.

#### Entities

It has some extra entities that can be used in automations:

* **Volume Aligned Binary Sensor**, on when all speakers / groups have the same volume.
* **Title Aligned Binary Sensor**, on when all speakers / groups have the title.
* **Connected Binary Sensor**, on when all speakers are connected.
* **Speaker Sensor**, the UUID of the speaker to fetch the favourites from.

#### Not yet implemented

* [ ] Create a service to set the Favourite

### NHC Basic Alarm Action & NHC Panic Mode Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

This action is exposed as alarm control panel.

### NHC BellButton Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

This action exposes a button and a lock.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, which represents the Basic State. It is on when bell button is press, off when no call
  is active.
* **Decline Call Applied On All Devices Binary Sensor**, which represents the Decline Call Applied On All Devices state.

### NHC Dimmer Action

This action is exposed as a light.

#### Entities

* **Aligned Binary Sensor**, this is on when:
    * all dimmers are on and have the same brightness
    * all dimmers are off, regardless of the brightness

#### Services

The integration exposes a service to set the brightness of a light. This can be
used to set the brightness without turning the lights on. For instance if you want
your lights to have a certain brightness at night. See Developer Tools → Services → Niko Home Control II: Set brightness
for light.

### NHC Fan Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

This is exposed as a fan entity.

### NHC Free Start Stop Actions

This action is exposed as a button.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, is on according to the state of all assigned players as configured for that action.
* **Start Active Binary Sensor**, is on upon activation of the action. It is off when one of the assigned participant in
  the action has a state change.

### NHC Garage Door Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

#### Entities

* **Basic State Enum Sensor**, which represents the Basic State. On means the gate is opened, off means the gate is
  closed. Intermediate means the gate is moving, only when optional moving sensor is available.

### NHC House Mode Actions (untested)

__Remark:__ this is untested as I don't own a device of this type.

This action is exposed as a button.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, is on according to the state of all assigned players as configured for that action.
* **Start Active Binary Sensor**, is on upon activation of the action. It is off when one of the assigned participant in
  the action has a state change.

### NHC HVAC Thermostat (untested)

__Remark:__ this is untested as I don't own a device of this type.

This is exposed as a climate entity.

#### Todo

* [ ] see todo's from NHC Thermostat

#### Entities

* **Setpoint Temperature Sensor**, the desired setpoint in the current program.
* **Overrule Active Switch**, marks if the overrule-time will be used instead of setpoint as defined in program mode.
* **Overrule Setpoint Temperature Sensor**, the current overruled setpoint temperature.
* **Overrule Time Duration Sensor**, duration of the overrule period in minutes.
* **EcoSave Switch**, marks if the EcoSave mode is active. When active the program keeps going, but the
  setpointtemperature is altered (+3 when cooling, -3 when heating).
* **Protect Mode Switch**, marks if the Protect mode is active. This is the system off mode with temperature protection.
  Heating is activated when temperature is too low Cooling is activated when temperature is too high.
* **Thermostat on Switch**, indicates wheter the thermostat is turned on or off.
* **HVAC On Binary Sensor**, indicates that the HVAC indoor unit is online.

### NHC Thermostat (untested)

__Remark:__ this is untested as I don't own a device of this type.

This is exposed as a climate entity.

#### Todo

* [ ] [Check if we can implement target_temperature_high, target_temperature_low, target_temperature_step](https://github.com/joleys/niko-home-control-II/blob/master/custom_components/nhc2/nhccoco/coco_climate.py#L103)
* [ ] [Check if we can implement max_temp, min_temp](https://github.com/joleys/niko-home-control-II/blob/master/custom_components/nhc2/nhccoco/coco_climate.py#L112)

#### Entities

* **Setpoint Temperature Sensor**, the desired setpoint in the current program.
* **Overrule Active Switch**, marks if the overrule-time will be used instead of setpoint as defined in program mode.
* **Overrule Setpoint Temperature Sensor**, the current overruled setpoint temperature.
* **Overrule Time Duration Sensor**, duration of the overrule period in minutes.
* **EcoSave Switch**, marks if the EcoSave mode is active. When active the program keeps going, but the
  setpointtemperature is altered (+3 when cooling, -3 when heating).

### NHC Mood Action

This action is exposed as a button.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, is on according to the state of all assigned players as configured for that action.
* **Mood Active Binary Sensor**, is on upon activation of the action. It is off when one of the assigned participant in
  the action had a state change.

### NHC Motor Action

This is exposed as a cover entity.

#### Entities

* **Aligned Binary Sensor**, this is on when all motors have the same position.
* **Moving Binary Sensor**, this is on when the any motor is running.
* **Last Direction Sensor** (undocumented).

### NHC PIR Action (untested)

__Remark:__ this is untested as I don't own a device of this type.

This action is exposed as a button.

#### Entities

It has some extra entities that can be used in automations:

* **Basic State Binary Sensor**, is on when motion detection is enabled, off when disabled.

### NHC Virtual flag (untested)

__Remark:__ this is untested as I don't own a device of this type.

This is exposed as switch.

### NHC Relay Action (light, socket, switched-fan, switched-generic)

Lights are exposed as lights. Others are exposed as switches.

### NHC Zigbee Smart plug

This is the energy metering linked to a zigbee smart plug. The smart plug itself is a different device.

#### Entities

* **Electrical Power Sensor**, the realtime power usage in W. Positive means power consumed, negative is power
  produced.
* **Report Instant Usage Binary Sensor**, indicates if the Electrical Power is received. When disabled, it will
  automatically be enabled.
* **Feedback Enabled Binary Sensor**. On if the feedback led shows the relay status. Off if the feedback led is
  disabled.
* **Measuring Only Binary Sensor**. If on, the relay will always be on.

#### Remarks

The totals are not available as they are not (yet) exposed by the API.

### Generic Zigbee Smart plug (untested)

__Remark:__ this is untested as I don't own a device of this type.

This is the energy metering linked to a generic zigbee smart plug. The smart plug itself is a different device.

#### Entities

* **Electrical Power Sensor**, the realtime power usage in W. Positive means power consumed, negative is power
  produced.
* **Report Instant Usage Binary Sensor**, indicates if the Electrical Power is received. When disabled, it will
  automatically be enabled.

#### Remarks

The totals are not available as they are not (yet) exposed by the API.

### Electricity Metering module (with clamp) (untested)

__Remark:__ this is untested as I don't own a device of this type.

#### Entities

* **Electrical Power Sensor**, the realtime power usage in W. Possitive means power consumed, negative is power
  produced.
* **Report Instant Usage Binary Sensor**, indicates if the Electrical Power is received. When disabled, it will
  automatically be enabled.
* **Flow Sensor**. Producer or Consumer
* **Segment Sensor**. Central or Subsegment
* **Clamp Type Sensor**. 63A or 120A

### Energy Home (untested)

__Remark:__ this is untested as I don't own a device of this type.

#### Entities

* **Electrical Power to Grid Sensor**, the realtime power usage in W as a sum for all central meters.
* **Electrical Power from Grid Sensor**, the realtime power consumption in W as a sum for all central meters.
* **Electrical Power Production Sensor**, the realtime power production in W as a sum for all producers.
* **Electrical Power Self Consumption Sensor**, electrical power production minus power to grid.
* **Electrical Power Consumption Sensor**, electrical power self production + electrical power from grid.
* **Report Instant Usage Binary Sensor**, indicates if the Electrical Power is received. When disabled, it will
  automatically be enabled.
* **Electrical Power Production Threshold Exceeded Binary Sensor**, this is on when the central meters electrical power
  production is greater than the threshold of 300W (+ 5W hysteresis)

## Not yet supported

* NHC Touch Switch
* NHC Presence Simulation Action
* NHC Reynaers Action
* NHC Velux Action
* Sonos Speaker
* Bose Speaker
* Generic Ventilation Implementation
* Generic Heating/Cooling Implementation
* Generic Warm Water Implementation

## How to get it running

Note: Make sure you have a recent version of Home Assistant!

1. Install this custom component
2. Go to Configuration > Integrations
3. Add an integration, search for Niko Home Control II, and click on it
4. Follow the wizard

## Adding an Energy Meter?

This currently requires some manual action in your configuration.yaml.

You need to add (and possibly tweak) the following:

    sensor:
        - platform: integration
            source: sensor.elektriciteitsmeting
            name: energy_elektriciteit
            unit_prefix: k
            round: 3
            method: left

    utility_meter:
        energy_daily:
            source: sensor.energy_elektriciteit
            cycle: daily
        energy_monthly:
            source: sensor.energy_elektriciteit
            cycle: monthly

## Development

### Adding support for new Device models

* Add a new class for the device in `nhccoco/devices`. The name of the file is `{model}_{type}.py`. The classname is
  `Coco{Model}{Type}`.
* Import the class in `nhccoco/coco.py`. This allows the Coco class to create an instance when the device is present in
  the device list.
* Create the needed entities in `entities`
* Add the entities that should be created in the correct platform-file.

## Found a bug?

When and if you find a bug, please document it as good as possible (how to reproduce, logs, screenshots, etc)

## Want to help?

Make a PR, contact me, test new releases, code new entities ...
