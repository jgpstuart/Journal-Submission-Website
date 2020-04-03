from django.shortcuts import render
from django.views import generic
from userPages.models import Paper, Journal, Proposal, Institution, Comment
from home.models import User


def author(request):
    function1 = "Submissions"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/authorSubmit"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'authorDashboard.html', args)


def reviewer(request):
    function1 = "Submitted Papers"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewSubmissions"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'reviewerDashboard.html', args)


def editor(request):
    function1 = "Paper Reviews"
    function2 = "Journals"
    function3 = "Profile"
    function4 = "Logout"
    dashVariable = "/viewReviews"

    args = {'Function4': function4, 'Function1': function1, 'Function2': function2, 'Function3': function3,
            'dashVariable': dashVariable}
    return render(request, 'editorDashboard.html', args)


def reviewer_view_proposals(request):
    # Generate counts for proposals
    num_proposals = Proposal.objects.all().count()

    # Filter by reviewer
    # num_proposal_correct_reviewer = Proposal.objects.filter(reviewer_1 = me).count()
    # num_proposal_correct_reviewer = Proposal.objects.filter(reviewer_2=me).count()
    # num_proposal_correct_reviewer = Proposal.objects.filter(reviewer_3=me).count()

    context = {
        'num_proposals': num_proposals,
    }

    return render(request, 'reviewerListViewPage.html', context=context)


class ReviewerProposalListView(generic.ListView):
    model = Proposal
    context_object_name = 'Proposals to Review'
