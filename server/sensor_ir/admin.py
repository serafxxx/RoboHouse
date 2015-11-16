from models import IRModule, IRRemoute, IRCommand
from django.contrib import admin


@admin.register(IRModule)
class IRmoduleAdmin(admin.ModelAdmin):
    pass

@admin.register(IRRemoute)
class IRRemouteAdmin(admin.ModelAdmin):
    pass

@admin.register(IRCommand)
class IRCommandAdmin(admin.ModelAdmin):
    pass
