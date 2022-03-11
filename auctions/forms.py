from django.forms import ModelForm
from .models import *


class CreateListingForm(ModelForm):
    class Meta:
        model = CreateListing
        fields = ['title', 'description', 'imageUrl', 'startBid', 'category', 'active', 'date']

class BidForm(ModelForm):
  class Meta:
    model = Bid
    fields = ["offer"]
    
class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ["comment"]