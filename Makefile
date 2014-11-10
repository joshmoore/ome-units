# exclude Angle
files: units/UnitsElectricPotential.units UnitsFrequency.units units/UnitsLength.units units/UnitsPressure.units units/UnitsPower.units units/UnitsTemperature.units units/UnitsTime.units
model: model/UnitsElectricPotential.java model/UnitsFrequency.java model/UnitsLength.java model/UnitsPressure.java model/UnitsPower.java model/UnitsTemperature.java model/UnitsTime.java
sql: sql/UnitsElectricPotential.sql sql/UnitsFrequency.sql sql/UnitsLength.sql sql/UnitsPressure.sql sql/UnitsPower.sql sql/UnitsTemperature.sql sql/UnitsTime.sql

model/%.java: units/%.txt
	mkdir -p model
	./gen.py $< templates/model > $@

sql/%.sql: units/%.txt
	mkdir -p sql
	./gen.py $< templates/sql > $@

clean:
	rm -rf model/* sql/*

.PHONY: sql files model clean
