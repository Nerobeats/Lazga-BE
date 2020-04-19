from rest_framework.permissions import BasePermission


class IsNotSubmitted(BasePermission):
	message = "Order is already submitted , please contact us through email"

	def has_object_permission(self, request, view, obj):
		if (request.user.is_staff) or ((obj.order.user == request.user) and (obj.order.status == "NS")):
			return True
		else:
			return False

class IsOwner(BasePermission):
	message = "You must be the owner of this Order"

	def has_object_permission(self, request, view, obj):
		return request.user.is_staff or (obj.user == request.user)
		
