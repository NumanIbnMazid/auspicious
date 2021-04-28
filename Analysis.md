# Links:
    - https://auspiciousbd.com/
    - https://www.figma.com/proto/7AkbUWD8SMe6g9a5lx1H2y/Auspicous-Website?node-id=27%3A181&viewport=1536%2C-516%2C0.32453566789627075&scaling=min-zoom


# Dynamic Pages

    * Projects
        - Project Name
        - Client Name
        - Development Year (Start Year (non-nullable) - Ending Year (nullable))
        - Scope (Short Description) (Rich Text Editor) (Unlimited Character)
        - Status (Completed/Ongoing)
        - Image (nullable) (png, jpeg) (5 MB Max)

        [
            - Latest Project (Sortable) (Limit 12)
            - Project Detail Page
        ]

    * News Category
        - Title
        - Image
        - Timestamp

    * Latest News
        - Title
        - Category (News Category - FK)
        - Description (Rich Text Editor) (Unlimited Character)
        - Image (png, jpeg) (5 MB Max)
        - Timestamp

        [
            - Latest News (Sortable) (Limit 12)
        ]

    * News Comment (Logged In User)

    * Gallery
        - Image (png, jpeg) (5 MB Max)
        - Timestamp

    * Clients
        - Name
        - Logo
        - Category (Sister Concern, Enlistment, Local Representative, Civil, Telecom)
        - Timestamp

        [
            On Click -> Client and Sister Concer page (Client and Sister Concern List)
        ]

    * Contact
        - Phone
        - Email
        - Address

        [
            - Map
        ]
    
    * Social Account
        - Title
        - Logo
        - Link

    * Job Position
        - Title
        - Timestamp

    * Career
        - User (FK)
        - Job Position (Job Position - FK)
        - File (CV-PDF, DOC)
        - Status (Pending, Review, Confirmed, Rejected)
        - Timestamp
        [
            - Access (Must Logged In)
            - CV Drop (PDF, DOC)
            - Status (Admin Panel) -> Mail Send -> SMS (Confirmed - Interview Call)
            - Apply BTN (On All State)
            - Single User can Apply Multiple Time
        ]

    * User Type
        - Super Admin
        - Admin
        - Regular User

        [
            - Super Admin can create admin and assign to a group
        ]

    * User Group
        - Title
        - Permisssions
        - User

        [
            - Super Admin (Access)
        ]

    * User
        - Username
        - Email
        - Password
        - Phone Number
        - First Name
        - Last Name

        [
            - Password Update
            - Password Reset
            - Forgot Password
        ]