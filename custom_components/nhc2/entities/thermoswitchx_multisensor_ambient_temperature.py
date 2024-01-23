from homeassistant.components.sensor import SensorEntity, SensorDeviceClass, SensorStateClass
from homeassistant.const import UnitOfTemperature

from ..const import DOMAIN, BRAND

from ..nhccoco.devices.thermoswitchx_multisensor import CocoThermoswitchxMultisensor


class Nhc2ThermoswitchxMultisensorAmbientTemperatureEntity(SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoThermoswitchxMultisensor, hub, gateway):
        """Initialize a sensor."""
        self._device = device_instance
        self._hub = hub
        self._gateway = gateway

        self._device.after_change_callbacks.append(self.on_change)

        self._attr_available = self._device.is_online
        self._attr_unique_id = device_instance.uuid + '_ambient_temperature'
        self._attr_should_poll = False

        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_native_value = self._device.ambient_temperature
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_suggested_display_precision = 1
        self._attr_native_precision = 1

    @property
    def name(self) -> str:
        return 'Ambient Temperature'

    @property
    def device_info(self):
        """Return the device info."""
        return {
            'identifiers': {
                (DOMAIN, self._device.uuid)
            },
            'name': self._device.name,
            'manufacturer': f'{BRAND} ({self._device.technology})',
            'model': str.title(f'{self._device.model} ({self._device.type})'),
            'via_device': self._hub
        }

    @property
    def native_value(self) -> int:
        return self._device.ambient_temperature

    def on_change(self):
        self.schedule_update_ha_state()
