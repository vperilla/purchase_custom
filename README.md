# purchase_custom
Sample Odoo purchase customization

On this sample I add an a new field called "Request Reference" underneath "Vendor Reference",
and also Order Deadline date must be invisible when "Request Reference" equals to "ABC".

This repository can be tested on Odoo 12 Version, but the logic also apply to other versions like 10.

Also can be tested with Docker with the following steps:

1) If you dont have an database ready:

docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:10
docker start db

2) And then craete an container using this module
docker run -v /path/to/purchase_custom_addon:/mnt/extra-addons -p 8069:8069 --name odoo --link db:db -t odoo
