from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections
from .models import User, Home, Customer

@registry.register_document
class HomeDocument(Document):
    user = fields.ObjectField()
    customer = fields.NestedField(properties={
    'budget': fields.IntegerField(),
    
    })
    
    class Index:
        # Name of the Elasticsearch index
        name = 'home'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 1}

    class Django:
        model = Home # The model associated with this Document
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'create_time',
            'modified_time',
            'name',
            'phone',
            'address',
            'square_meter',
            'property_type',
            'doc_type',
            'age',
            'parking',
            'elevator',
            'telephone',
            'warehouse',
            'balcony',
            'terrace',
            'price',

        ]
        related_models = [User, Customer]

        
@registry.register_document
class CustomerDocument(Document):
    
    class Index:
        # Name of the Elasticsearch index
        name = 'customer'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 1}

    class Django:
        model = Customer # The model associated with this Document
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'create_time',
            'modified_time',
            'budget',

        ]
        # related_models = [Home]
        
        