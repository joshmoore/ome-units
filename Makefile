all: blitz/Units.ice blitz2 blitz3 blitz4 formats/UnitsFactory.java model model2 sql

# exclude Angle
units ?= units/ElectricPotential.txt units/Frequency.txt  units/Length.txt  units/Pressure.txt  units/Power.txt  units/Temperature.txt  units/Time.txt
files: $(units)

model:  model/UnitsElectricPotential.java model/UnitsFrequency.java model/UnitsLength.java model/UnitsPressure.java model/UnitsPower.java model/UnitsTemperature.java model/UnitsTime.java
model2: model2/ElectricPotential.java     model2/Frequency.java     model2/Length.java     model2/Pressure.java     model2/Power.java     model2/Temperature.java     model2/Time.java
sql:    sql/UnitsElectricPotential.sql    sql/UnitsFrequency.sql    sql/UnitsLength.sql    sql/UnitsPressure.sql    sql/UnitsPower.sql    sql/UnitsTemperature.sql    sql/UnitsTime.sql
blitz2: blitz/ElectricPotential.ice       blitz/Frequency.ice       blitz/Length.ice       blitz/Pressure.ice       blitz/Power.ice       blitz/Temperature.ice       blitz/Time.ice
blitz3: blitz/ElectricPotentialI.java     blitz/FrequencyI.java     blitz/LengthI.java     blitz/PressureI.java     blitz/PowerI.java     blitz/TemperatureI.java     blitz/TimeI.java
blitz4: blitz/omero_model_ElectricPotentialI.py     blitz/omero_model_FrequencyI.py     blitz/omero_model_LengthI.py     blitz/omero_model_PressureI.py     blitz/omero_model_PowerI.py     blitz/omero_model_TemperatureI.py     blitz/omero_model_TimeI.py

blitz/Units.ice: $(units)
	mkdir -p blitz
	./gen.py --combine templates/Units.ice $(units) > $@

formats/UnitsFactory.java: $(units)
	mkdir -p formats
	./gen.py --combine templates/formats.java $(units) > $@

blitz/%.ice: units/%.txt
	mkdir -p blitz
	./gen.py templates/blitz.ice $< > $@

blitz/%I.java: units/%.txt
	mkdir -p blitz
	./gen.py templates/blitz.java $< > $@

blitz/omero_model_%I.py: units/%.txt
	mkdir -p blitz
	./gen.py templates/blitz.py $< > $@

model/Units%.java: units/%.txt
	mkdir -p model
	./gen.py templates/model $< > $@

model2/%.java: units/%.txt
	mkdir -p model2
	./gen.py templates/model.java $< > $@

sql/Units%.sql: units/%.txt
	mkdir -p sql
	./gen.py templates/sql $< > $@

clean:
	rm -rf blitz formats model model2 sql

.PHONY: sql files model clean
