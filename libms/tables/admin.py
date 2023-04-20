from django.contrib import admin
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from import_export import resources





tables_models = apps.get_app_config('tables').get_models()
A = "Admin"
R = "Resource"

for m in tables_models:
	mr =str(m) + R
	ma = str(m) + A
	class mr(resources.ModelResource):
		class Meta:
			model = m

	class ma(ImportExportModelAdmin):
		resource_class = mr

	admin.site.register(m, ma)