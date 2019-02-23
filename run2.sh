#!/bin/bash

readonly name=tests
readonly version=latest
readonly data_volume=data_${name}
readonly image=registry.business-hub.com/odoo/odoo11

readonly pghost=172.17.0.1
readonly pguser="odoo"
readonly pgport=5433
readonly pgpassword="odoo"
readonly admin_passwd="admin"
readonly scriptpath=`dirname $0`

set -u

docker run --rm -it \
       --name=${name} \
       -p 8069:8069 \
       -e PGHOST=${pghost} \
       -e PGUSER=${pguser} \
       -e PGPORT=${pgport} \
       -e PGPASSWORD=${pgpassword} \
       -e ADMIN_PASSWD=${admin_passwd} \
       -e ENTERPRISE=1 \
       -e EXTRA_ADDONS="/opt/odoo/extra-addons/custom" \
       -v ${data_volume}:/var/lib/odoo \
       -v `realpath $scriptpath`/odoo/addons:/opt/odoo/extra-addons/custom \
       ${image}:${version} -d dev_tests2 $@
