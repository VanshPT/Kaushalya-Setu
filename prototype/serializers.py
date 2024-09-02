from rest_framework import serializers

class PromptSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True)

    def validate_prompt(self, value):
        # Add any custom validation logic for the prompt here
        if len(value) < 5:
            raise serializers.ValidationError("Prompt must be at least 5 characters long.")
        return value