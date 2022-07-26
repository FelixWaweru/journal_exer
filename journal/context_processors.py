from .models import Entry

# def prev_entries(request):
#     # Only works if user is logged in
#     if request.user.is_authenticated:
#         try:
#             entry = Entry.objects.get(user=request.user)
#             return {
#                 'entries': entry
#             }
#         except:
#             return {
#                 'entries': ''
#             }
#     else:
#         return {
#             'entries': ''
#         }
