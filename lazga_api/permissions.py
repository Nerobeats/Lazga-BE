from rest_framework.permissions import BasePermission


class IsNotSubmitted(BasePermission):
	message = "Order is already submitted , please contact us through email"

	def has_object_permission(self, request, view, obj):
		if (request.user.is_staff) or ((obj.user == request.user) and (obj.status != "NS")):
			return True
		else:
			return False