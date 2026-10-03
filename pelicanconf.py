AUTHOR = 'Patrick Williams'
SITENAME = 'Patrick Williams | Analytics & BI Leader'
SITEURL = 'https://www.weeyums.com'

PATH = 'content'

# Custom domain: copy CNAME to the site root so GitHub Pages keeps it on every deploy
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/dark-portfolio'

# Disable blog features we don't need
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# No blog posts — pages only
DEFAULT_PAGINATION = False

# Template for the home page
DIRECT_TEMPLATES = ['index']
PAGINATED_TEMPLATES = {}

# ── PROFILE ──────────────────────────────────────────────────────────────────
PROFILE = {
    'name': 'Patrick Williams',
    'title': 'Manager & Strategist — Sales & Marketing Analytics',
    'tagline': 'Turning complex data into clear, compelling decisions that drive commercial growth.',
    'email': 'patrick.weeyums@gmail.com',
    'linkedin': 'https://www.linkedin.com/in/patrick-weeyums',
    'powerbi_url': '#portfolio',  # Replace with your live Power BI report URL
    'headshot': '',              # Set to filename e.g. 'headshot.jpg' once you have an image
                                 # and place the file in themes/dark-portfolio/static/images/
}

# ── ABOUT ─────────────────────────────────────────────────────────────────────
ABOUT = {
    'paragraphs': [
        "Seasoned data leader with 15+ years of success enhancing commercial, marketing, and sales operations at companies of all sizes and growth stages — spanning retail, e-commerce, pharmaceutical, and medical device.",
        "I excel as both a builder and leader of advanced analytics teams and as a hands-on analyst who can dive in and add immediate value. My work sits at the intersection of rigorous data analysis and strategic business thinking, translating complex datasets into clear stories that executives and field teams can act on.",
        "Strong executive presence and holistic business acumen refined through entrepreneurial ventures, consulting engagements, and formal MBA and MSA training from UNC Chapel Hill and NC State University.",
    ],
    'stats': [
        {'number': '15+', 'label': 'Years Experience'},
        {'number': '15+', 'label': 'Power BI Dashboards Built'},
        {'number': '4', 'label': 'Industries Served'},
        {'number': '$375M+', 'label': 'Revenue Under Analytics'},
    ],
}

# ── EXPERIENCE ────────────────────────────────────────────────────────────────
EXPERIENCE = [
    {
        'company': 'Solta Medical (Bausch Health)',
        'role': 'Senior Manager, Marketing Analytics',
        'dates': 'Feb 2019 – Present',
        'bullets': [
            'Built a Power BI reporting suite of 15+ interactive dashboards covering weekly sales performance, customer churn, reorder rates, and key activity metrics — ranked 5th most utilized package across the entire Bausch Health Power BI server.',
            'Designed and launched a subscription sales model for the consumables business; 105 accounts enrolled in year one (25% of total sales), growing 2.5× faster than non-subscription accounts.',
            'Automated real-time territory reporting by partnering with Bausch IT to build a SQL database from Salesforce data, replacing error-prone manual Excel processes for ~80 field reps.',
            'Developed systematic bottom-up forecasting techniques that improved accuracy of forecasts produced by finance teams.',
        ],
    },
    {
        'company': 'GlaxoSmithKline (GSK)',
        'role': 'Sales Analytics Manager, Respiratory Biologics',
        'dates': 'Apr 2018 – Jan 2019',
        'bullets': [
            'Developed an interactive Tableau dashboard that standardized and automated a weekly diagnostic process, summarizing performance toward reach, frequency, Rx volume, and writer count goals in a $300M business unit.',
            'Led implementation of 10+ IQ20/20 software enhancements that increased precision of sales tracking and created visibility into the specialty pharmacy channel.',
            'Improved field sales recruitment targeting by identifying 6,000 healthcare providers with a strong propensity to attend live speaker programs.',
        ],
    },
    {
        'company': 'GlaxoSmithKline (GSK)',
        'role': 'Advanced Analytics Analyst, Primary Care',
        'dates': 'May 2015 – Mar 2018',
        'bullets': [
            'Co-built and deployed a marketing mix model with Tableau dashboards featuring response curves representing incremental profit from investment across marketing channels and geographies.',
            'Automated a physician-level prescribing behavior aggregation program using R statistical analysis, sending weekly performance reports to 2,000+ sales reps.',
            'Built a Tableau tracking template that isolated the performance impact of sales pilot programs at a regional level.',
        ],
    },
    {
        'company': 'Hanesbrands',
        'role': 'Senior Marketing Analyst, Web Analytics',
        'dates': 'Nov 2010 – Jun 2014',
        'bullets': [
            'Managed all data collection, reporting, and analysis for four e-commerce sites in partnership with BI, marketing leadership, and executive stakeholders.',
            'Led a data warehousing initiative to consolidate keyword-level data into a single SQL + Tableau reporting stack, dramatically expanding SEO analysis granularity.',
            'Implemented an automated cross-sell engine across all websites, driving a 500% increase in cross-sell buyers.',
        ],
    },
]

# ── SKILLS ────────────────────────────────────────────────────────────────────
SKILLS = [
    {
        'category': 'Data Visualization',
        'icon': '📊',
        'tools': ['Microsoft Power BI', 'Tableau', 'DAX & Power Query (M)', 'Python (Pandas)'],
    },
    {
        'category': 'Data & Languages',
        'icon': '💻',
        'tools': ['SQL', 'Python', 'DAX', 'R (Statistical Analysis)', 'Salesforce CRM'],
    },
    {
        'category': 'Analytics & Strategy',
        'icon': '🧠',
        'tools': ['Revenue Forecasting', 'Marketing Mix Modeling', 'Market Research', 'Sales Incentive Compensation', 'Predictive & Regression Modeling'],
    },
    {
        'category': 'Leadership & Process',
        'icon': '🎯',
        'tools': ['Analytics Team Leadership', 'Process Automation', 'Executive Storytelling', 'Vendor Management', 'Coaching & Mentoring'],
    },
]

# ── POWER BI PORTFOLIO ────────────────────────────────────────────────────────
POWERBI_PROJECTS = [
    {
        'title': 'Field Sales Reporting Suite',
        'description': 'Designed 15 Power BI reports from scratch for Solta Medical field reps — covering territory performance, cold account identification, promo utilization, and forecasting. Ranked 5th most-utilized package on the Bausch Health server out of thousands.',
        'tags': ['Power BI', 'SQL', 'Salesforce', 'Sales Analytics'],
    },
    {
        'title': 'Executive Performance Dashboard',
        'description': 'Built 15+ interactive Power BI dashboards for senior leadership tracking weekly sales performance, customer churn, reorder rates, and key activity metrics across a $75M North American business unit.',
        'tags': ['Power BI', 'DAX', 'Executive Reporting', 'KPI Tracking'],
    },
    {
        'title': 'Subscription Sales Model Analysis',
        'description': 'Analyzed feasibility and designed a new subscription pricing model for consumables. In year one, 105 accounts enrolled — 25% of total sales — growing 2.5× faster than standard accounts.',
        'tags': ['Financial Modeling', 'Power BI', 'Growth Strategy'],
    },
]
