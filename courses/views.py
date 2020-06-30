from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from GEN.decorators import course_enrollment_check
from GEN.support_methods import enrollment_test

from courses.support_methods import requirement_fulfilled
from .models import Course, Section, SectionItem
from .progress import progress


not_enrolled_error = _("You are not enrolled in the requested course.")


@login_required
@course_enrollment_check(enrollment_test)
def course(request, pk):
    course_object = get_object_or_404(Course, pk=pk)
    sections = course_object.sections.filter(published=True)
    discussions = course_object.discussions.all()
    quizzes = course_object.quizzes.all()
    # user = request.user
    # TODO: improve this: I've hard-corded this section name because
    # info isn't a dynamic section item
    section_name = "Info"

    # check_user_enrollment(request, user, course_object)

    # progress status
    discussions_progress = progress(request, discussions)
    quizzes_progress = progress(request, quizzes)

    return render(
        request,
        "course.html",
        {
            "course": course_object,
            "sections": sections,
            "section_name": section_name,
            "discussions_progress": discussions_progress,
            "quizzes_progress": quizzes_progress,
        },
    )


@login_required
@course_enrollment_check(enrollment_test)
def section_page(request, pk, section_pk):
    course_object = get_object_or_404(Course, pk=pk)
    section_object = get_object_or_404(Section, pk=section_pk)
    section_items = section_object.section_items.filter(published=True)
    gamification = course_object.enable_gamification
    user = request.user
    requirement = section_object.requirement
    allow_submission = False
    start_date_reached = False
    end_date_passed = False

    # check_user_enrollment(request, user, course_object)

    # check if user is a course instructor
    is_instructor = bool(course_object in request.user.instructor.all())

    # check if section has start and end dates

    # check if section start date
    if section_object.start_date:
        if timezone.now() < section_object.start_date:
            if not is_instructor:
                messages.warning(
                    request,
                    _(
                        "This section's contents are not yet available because the start date has not been reached."
                    ),
                )
                # clear out section items
                section_items = SectionItem.objects.none()
            else:
                messages.info(
                    request,
                    _(
                        "This section and its contents are not yet available to participants because of the start date."
                    ),
                )
        else:
            start_date_reached = True

    # check section end date
    # FIXME: instead of totally hiding the content, maybe I could just disable the links
    if section_object.end_date:
        if timezone.now() > section_object.end_date:
            end_date_passed = True

            if not is_instructor:
                messages.warning(
                    request,
                    _(
                        "This section is closed and its contents have been hidden or disabled because the end date has passed."
                    ),
                )
                # clear out section items
                section_items = SectionItem.objects.none()
            else:
                messages.info(
                    request,
                    _(
                        "This section is closed and its contents have been hidden or disabled to participants because the end date has passed."
                    ),
                )

    # only allow participant to access section if requirements have been fulfilled
    if requirement and not is_instructor:
        fulfilled = requirement_fulfilled(user, section_object)

        if not fulfilled:
            messages.error(
                request,
                _(
                    "You have not fulfilled the requirements to access the requested section."
                ),
            )
            return redirect("course", pk=course_object.pk)

    if section_object.section_type == "Q":
        section_template = "section_quiz.html"
    elif section_object.section_type == "D":
        section_template = "section_discussion.html"
    elif section_object.section_type == "V":
        if is_instructor:
            # getting all section items (even not published)
            section_items = section_object.section_items
        section_template = "section_videos.html"
    elif section_object.section_type == "U":
        section_template = "section_upload.html"
        # getting all section items (even not published) and filtering by user
        section_items = section_object.section_items.filter(author=request.user)
        # if there is no section item, allow submission
        if section_object.start_date:
            if not section_items and start_date_reached:
                allow_submission = True
        elif section_object.end_date:
            if not section_items and end_date_passed:
                allow_submission = True
        else:
            if not section_items:
                allow_submission = True

    return render(
        request,
        section_template,
        {
            "course": course_object,
            "section": section_object,
            "section_items": section_items,
            "gamification": gamification,
            "allow_submission": allow_submission,
        },
    )
