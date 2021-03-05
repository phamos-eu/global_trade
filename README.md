# General

Global Trade is an App for ERPNext in which further aspects for international/global trade are concidered.

# Install

Go the the frappe-bench folder and install the app:

cd frappe-bench

bench get-app https://github.com/tueit/global_trade.git

bench --site erp.my-company.com install-app global_trade (where erp.my-company.com is your custom site name)

After the code has run re-set permissions within the frappe-bench folder with

chown -R frappe:frappe *

Then run a

bench migrate && bench build

bench restart

Once finished you should see Global Trade on you dashboard.

If you have any question, please create an issue.

#### License

MIT
