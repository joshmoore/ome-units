sql: sql/Angle sql/ElectricPotential sql/Frequency sql/Length sql/Pressure sql/Power sql/Temperature sql/Time

sql/%: units/%
	mkdir -p sql
	cut -f1 $< | \
	xargs | \
	sed "s/[^ ][^ ]*/'&'/g" | \
	perl -pe s'/\s/,/g' | \
	sed 's/\(.*\)/CREATE TYPE UnitsXXX AS ENUM { \1 };\n/g' > $@
	perl -i -pe "s/XXX/$$(basename $<)/" $@

clean:
	rm -rf sql/*

.PHONY: sql clean
