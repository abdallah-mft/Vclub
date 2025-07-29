
from django.contrib import admin, messages
from .models import Club, ClubRequest

@admin.register(ClubRequest)
class ClubRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_approved', 'president']
    list_filter = ['is_approved']
    actions = ['approve_clubs']

    def approve_clubs(self, request, queryset):
        """
        Approves selected club requests and creates Club objects from them.
        """
        approved_count = 0
        
        # We will iterate over requests that are not yet approved
        for req in queryset.filter(is_approved=False):
            # 1. Check if a club with this username already exists to avoid errors
            if Club.objects.filter(username=req.username).exists():
                self.message_user(
                    request,
                    f"A club with the username '{req.username}' already exists. Request for '{req.name}' was skipped.",
                    level=messages.WARNING
                )
                continue

            # 2. Create the new club object
            # We exclude ManyToMany fields for now, as they need to be added after creation.
            new_club = Club.objects.create(
                name=req.name,
                username=req.username,
                slug=req.slug,
                description=req.description,
                wilaya=req.wilaya,
                university=req.university,
                founded_at=req.founded_at,
                is_active=True,  # Set the new club as active
                category=req.category,
                logo=req.logo,
                president=req.president,
                vice_president=req.vice_president,
                custom_fields=req.custom_fields,
            )

            # 3. Add the ManyToMany relationships
            # The .set() method is used to link the departments from the request to the new club
            new_club.departments.set(req.departments.all())

            # 4. Mark the request as approved and save it
            req.is_approved = True
            req.save()
            approved_count += 1

        # 5. Provide clear feedback to the admin
        if approved_count > 0:
            self.message_user(
                request,
                f"{approved_count} selected request(s) have been approved and turned into clubs.",
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                "No new clubs were approved. They may have already been approved or have conflicting usernames.",
                level=messages.INFO
            )

    approve_clubs.short_description = "Approve selected club requests"