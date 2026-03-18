from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['_id'] = str(ret['_id'])
        return ret
    class Meta:
        model = User
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['_id'] = str(ret['_id'])
        return ret
    class Meta:
        model = Team
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['_id'] = str(ret['_id'])
        return ret
    class Meta:
        model = Activity
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['_id'] = str(ret['_id'])
        return ret
    class Meta:
        model = Leaderboard
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if '_id' in ret:
            ret['_id'] = str(ret['_id'])
        return ret
    class Meta:
        model = Workout
        fields = '__all__'
