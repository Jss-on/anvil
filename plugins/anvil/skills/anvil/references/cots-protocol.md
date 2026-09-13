# Components, modules and sourcing

Use a pinned catalog with exact MPN/module identity, manufacturer, datasheet/revision, quote or
distributor, price/currency at quantity, stock/lead-time observation date, lifecycle state,
approved alternatives and application limits. Check provenance, footprint/pinout, firmware
interface, mass, voltage/current/thermal and mechanical envelope. A vendor marketing label is
not a worst-case rating or final-product certification.

`bom-cost` joins `MPN,Qty` BOM columns against unique `mpn,unit_price,currency` catalog rows.
Quantities must be positive integers; explicit DNP lines are excluded. Missing/duplicate parts,
malformed quantities, negative prices and mixed currencies fail. Declare PCB fabrication,
assembly and other product costs separately instead of hiding them inside a component price.

`bom/product-bom.csv` requires `item_id,category,qty,unit_price,currency,mass_g,source`.
Categories: pcb, cots, mech, fastener, wire, consumable, spare. Quantity is positive; price and
mass are nonnegative. `source` is a path relative to the BOM plus `#item_id`, for example
`../catalog/product-sources.csv#MOTOR-1`. That pinned CSV contains `item_id,unit_price,currency,
mass_g` and the source/quote/date metadata. The checker joins the exact source row and rejects
price/mass/currency drift. Decimal quantities support cut wire/material lengths with a declared
unit basis. Mass zero needs an engineering rationale in the source record.

The product rollup includes every physical assembly item and declared spare separately. Reconcile
it with assembly instructions, CAD-derived mass and system budgets. Part-count reduction is not
an improvement if it removes a required protection or testability function.

Review supplier quality, counterfeit risk, approved alternates, process changes, capacity and
obsolescence throughout the lifecycle. Refresh catalogs as logged events, not during a cost
comparison. Substitutions require electrical, firmware, mechanical, manufacturing and regulatory
impact assessment. Read-only sourcing research can proceed; ordering, contacting suppliers or
publishing issues requires existing session authorization for those external actions.
