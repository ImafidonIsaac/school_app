from django.core.exceptions import PermissionDenied
from django.conf import settings

        # ('Admin', 'Admin'),('Principal','Principal'),('Staff','Staff'),
        # ('Parent','Parent'),('Student','Student'),)


#Check if the user is a parent
def parent(function):
    def wrap(request, *args, **kwargs):
        
        if request.user.account_type == "Parent":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


#Check if the user is a Principal
def principal(function):
    def wrap(request, *args, **kwargs):
        
        if request.user.account_type == "Principal":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap



#Check if the user is a Staff
def staff(function):
    def wrap(request, *args, **kwargs):
        
        if request.user.account_type == "Staff":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


#Check if the user is a Student
def student(function):
    def wrap(request, *args, **kwargs):
        
        if request.user.account_type == "Student":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


#Check if the user is a Admin
def admin(function):
    def wrap(request, *args, **kwargs):
        
        if request.user.account_type == "Admin":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap









#This view can only be access when the number of cart item is greater than zero


# # Check if the user trying to withdraw is the owner of the wallet
# def user_is_wallet_owner(function):
#     def wrap(request, *args, **kwargs):
#         wallet = Wallet.objects.get(pk=kwargs['pk'])
#         if wallet.user == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap




# #Check if the user can crud blog
# def crud_blog(function):
#     def wrap(request, *args, **kwargs):
        
#         if request.user.crud_blog == True:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap

# #Check if the user trying to view the object is the object creator
# def user_is_blog_creator(function):
#     def wrap(request, *args, **kwargs):
#         blog = Post.objects.get(pk=kwargs['pk'])
#         if blog.creator == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap


# #Check if the user trying to view the object is the object creator
# def user_is_bank_creator(function):
#     def wrap(request, *args, **kwargs):
#         bank = BankAccount.objects.get(pk=kwargs['pk'])
#         if bank.user == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap




# #Check if the user can crud shop
# def crud_shop(function):
#     def wrap(request, *args, **kwargs):
        
#         if request.user.crud_shop == True:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap

# # Check if the user trying to view the product is the product creator
# def user_is_product_creator(function):
#     def wrap(request, *args, **kwargs):
#         product = Product.objects.get(pk=kwargs['pk'])
#         if product.creator == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap





# #Check if the user can crud blog
# def crud_training(function):
#     def wrap(request, *args, **kwargs):
        
#         if request.user.crud_training == True:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap

# # Check if the user trying to view the training is the training creator
# def user_is_training_creator(function):
#     def wrap(request, *args, **kwargs):
#         training = Training.objects.get(pk=kwargs['pk'])
#         if training.creator == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap





# #Check if the user can crud blog
# def crud_service(function):
#     def wrap(request, *args, **kwargs):
        
#         if request.user.crud_service == True:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap

    
# # Check if the user trying to view the service is the service creator
# def user_is_service_creator(function):
#     def wrap(request, *args, **kwargs):
#         service = Service.objects.get(pk=kwargs['pk'])
#         if service.creator == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap






# #Check if the user can crud blog
# def crud_seminar(function):
#     def wrap(request, *args, **kwargs):
        
#         if request.user.crud_seminar == True:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap


# # Check if the user trying to view the seminar is the seminar creator
# def user_is_seminar_creator(function):
#     def wrap(request, *args, **kwargs):
#         seminar = Seminar.objects.get(pk=kwargs['pk'])
#         if seminar.creator == request.user:
#             return function(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#     wrap.__doc__ = function.__doc__
#     wrap.__name__ = function.__name__
#     return wrap














