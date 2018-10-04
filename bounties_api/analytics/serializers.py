from rest_framework import serializers

from .models import BountiesTimeline
from drf_queryfields import QueryFieldsMixin
from std_bounties.models import Tag


class BountiesTimelineSerializer(
        QueryFieldsMixin,
        serializers.ModelSerializer):
    class Meta:
        model = BountiesTimeline
        fields = "__all__"
        read_only_fields = (
            "bounties_issued",
            "fulfillments_submitted",
            "fulfillments_accepted",
            "fulfillments_pending_acceptance",
            "fulfillment_acceptance_rate",
            "bounty_fulfilled_rate",
            "avg_fulfiller_acceptance_rate",
            "avg_fulfillment_amount",
            "total_fulfillment_amount",
            "bounty_draft",
            "bounty_active",
            "bounty_completed",
            "bounty_expired",
            "bounty_dead",)


class TimelineTagSerializer(serializers.ModelSerializer):
    total_count = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ('name', 'normalized_name', 'total_count')

    def get_total_count(self, obj):
        return obj.get('total', 0)

    def get_name(self, obj):
        ranked_tags = self.context.get('ranked_tags', {})
        normalized_name = obj.get('normalized_name')
        name = ranked_tags.get(normalized_name, normalized_name)
        return name
