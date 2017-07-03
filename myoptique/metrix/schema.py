import graphene
from graphene_django.types import DjangoObjectType

from myoptique.metrix.models import Department, Metric


class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department


class MetricType(DjangoObjectType):
    class Meta:
        model = Metric


class Query(graphene.AbstractType):
    department = graphene.Field(DepartmentType,
                                id=graphene.Int(),
                                name=graphene.String())

    all_departments = graphene.List(DepartmentType)

    metric = graphene.Field(MetricType,
                            id=graphene.Int(),
                            name=graphene.String())

    all_metrics = graphene.List(MetricType)

    def resolve_all_departments(self, args, context, info):
        return Department.objects.all()

    def resolve_all_metrics(self, args, context, info):
        return Metric.objects.all()

    def resolve_department(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Department.objects.get(pk=id)

        if name is not None:
            return Department.objects.get(name=name)

        return None

    def resolve_metric(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Metric.objects.get(pk=id)

        if name is not None:
            return Metric.objects.get(name=name)

        return None
