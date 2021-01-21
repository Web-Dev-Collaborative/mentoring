from rest_framework import serializers, viewsets, permissions

from .models import Participant


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = [
            'id',
            'email',
            'role',
            'full_name',
            'manager',
            'approved',
            'time_availability',
            'org',
            'org_chart_distance',
            'org_level',
            'time_at_org_level',
            'interests',
            'track_change',
            'comments',
        ]


# ViewSets define the view behavior.
class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
