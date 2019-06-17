# CONFIGURAR FILTROS POR CAMPO CON FILTERSET

class CratersFilter(filters.FilterSet):
    
    latitude = filters.NumberFilter(name='data__latitude', lookup_expr='exact')
    latitude__lt = filters.NumberFilter(name='data__latitude', lookup_expr='lt')
    latitude__gt = filters.NumberFilter(name='data__latitude', lookup_expr='gt')
    latitude__isnull = filters.BooleanFilter(name='data__latitude', lookup_expr='isnull')
    # not sure if 'isnull' is a valid lookup for JSONFields - just demonstrating that 
    # different lookups expect different value types.
    age = filters.CharFilter(name='data__age', lookup_expr='exact')

## Documentación de apoyo 
```
https://django-filter.readthedocs.io/en/master/guide/rest_framework.html
```