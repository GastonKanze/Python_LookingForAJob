import requests

if __name__ == "__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    urls = ["https://www.camilyo.com/joinus-camilyo", "https://allstars-it.com/israel/careers/", "https://www.comeet.com/jobs/action-item/04.000", "https://www.armis.com/about/careers/", "https://arpeely.breezy.hr/", "https://breezometer.com/careers", "https://streamelements.com/careers",
    "https://akamai.dejobs.org/isr/jobs/", "https://allcloud.io/careers/", "https://www.allot.com/careers/careers-page/careers-search-results/?cr=Israel", "https://angel.co/company/anima-app/jobs", "https://www.comeet.com/jobs/scr/A3.003", "https://anzu.io/careers/", "https://argus-sec.com/careers/", "https://www.ui.co.il/en/jobs",
    "https://ann-education.typeform.com/to/fDT0dJ", "https://www.appsflyer.com/jobs/office/4007793002/haifa/", "https://www.appsflyer.com/jobs/office/4007790002/herzliya/", "https://www.aquasec.com/about-us/careers/", "https://www.fitness22.com/join-us", "https://sqream.com/about/careers/#openings", "https://www.tipranks.com/jobs",
    "https://aspectiva.com/careers", "https://www.atera.com/careers/", "https://www.au10tix.com/company/careers/", "https://www.augury.com/about/careers/", "https://bidalgo.com/careers/", "https://www.bigpanda.io/company/careers/", "https://whatify.ai/careers/", "https://www.steps.me/careers#Positions", "https://sundaysky.com/company/careers/",
    "https://www.comeet.com/jobs/autodesk/70.00D?coref=1.10.r43_40D&t=1585665433721", "https://www.auroralabs.com/company/#careers", "https://www.autofleet.io/careers", "https://www.bimpression.com/careers/","https://boards.greenhouse.io/bluevine?gh_src=22919ad43", "https://jobs.storemaven.com/jobs", "https://tap.pm/jobs/",
    "https://www.bringg.com/careers/", "https://www.capitolis.com/careers/",  "https://www.catonetworks.com/careers/", "https://cloudinary.com/jobs","https://codevalue.com/hr-main/","https://www.codota.com/careers", "https://jobs.lever.co/contentsquare?location=Tel-Aviv%2C%20Israel", "https://spot.io/careers/", "https://www.synamedia.com/careers/",
    "https://convizit.com/careers/","https://www.crazylabs.com/careers/israel/", "https://www.curv.co/careers/", "https://www.cyberbit.com/company/careers/","https://www.cybereason.com/careers/rd", "https://www.cybereason.com/careers/information-security", "https://jobs.lever.co/simpo", "https://www.simplex.com/join-us/",
    "https://www.cybereason.com/careers/product", "https://www.cybereason.com/careers/technical-operation", "https://www.diagnosticrobotics.com/jobs", "https://www.dia-analysis.com/careers", "https://guardio.breezy.hr/", "https://company.ironsrc.com/careers-tel-aviv/", "https://www.sentinelone.com/jobs/", "https://tandemg.com/open-positions/",
    "https://www.cybintsolutions.com/careers/", "https://cyesec.com/careers.html", "https://www.cymotive.com/join-the-team/", "https://www.cynet.com/careers/", "https://crossix.com/job-openings/", "https://www.direct-ex.co.il/career", "https://www.deepinstinct.com/careers/israel/", "https://www.cybersixgill.com/careers/",
    "https://dagshub.com/careers", "https://jobs.lever.co/d-fendsolutions", "http://careers.doit-intl.com/", "https://drivenets.com/careers/", "https://www.duda.co/es/careers", "https://boards.greenhouse.io/dynamicyield?gh_src=413febe81", "https://rnd.ebay.co.il/join-us/","https://edgify.bamboohr.com/jobs/", "https://www.solutotlv.com/#Positions",
    "https://www.etoro.com/about/careers/", "https://www.env0.com/careers", "https://careers.elementor.com/explore/", "https://eko.engineering/#careers", "https://getfabric.com/careers/co/rd/all/", "https://www.fireblocks.com/careers/", "https://www.fiverr.com/jobs/offices/tlv", "https://simbionix.com/company/job-opportunities/",
    "https://www.forescout.com/company/careers/open-positions/", "https://www.fyber.com/careers/","https://gett.com/il/careers/", "https://www.gloat.com/careers/tlv", "https://herolo.co.il/jobs", "https://healthy.io/careers/", "https://hailo.ai/careers/", "https://www.guardknox.com/we-are-hiring/",  "https://sourcedefense.com/company/careers/",
    "https://www.hypercube.ai/openings/", "https://www.ilyon.net/careers/", "https://www.imperva.com/company/careers/", "https://huuugegames.com/careers/?locations=tel-aviv", "https://intsights.com/company/careers", "https://www.intellforce.com/work-with-us", "https://www.inomize.com/careers-israel","https://www.inomize.com/copy-of-israel-netanya",
    "https://k-health.breezy.hr/?&location=Tel-Aviv,%20IL#positions", "https://klear.com/about/jobs", "https://makers.lemonade.com/", "https://www.kindite.com/careers/", "https://www.joytunes.com/careers", "https://corp.kaltura.com/company/careers/", "https://www.comeet.com/jobs/localize/33.00F", "https://www.saips.co.il/",
    "https://www.loris.ai/careers/", "https://www.lsports.eu/careers/", "https://www.lusha.co/careers/", "https://www.liveperson.com/company/careers", "https://www.madeiradata.com/careers", "https://www.comeet.com/jobs/matific/62.000", "https://monday.com/jobs", "https://www.mongodb.com/careers/locations/tel-aviv", "https://scopiolabs.com/careers/",
    "https://www.moonactive.com/careers/", "https://moovit.com/jobs/", "https://www.netomedia.com/positions.html", "https://www.novami.com/careers/open-positions/", "https://nuvoton.co.il/careers/", "https://www.omnisys.co.il/careers-2/", "https://www.oranbit.co.il/%D7%A7%D7%A8%D7%99%D7%99%D7%A8%D7%94/", "https://orantech.co.il/%d7%a7%d7%a8%d7%99%d7%99%d7%a8%d7%94/",
    "https://www.overwolf.com/jobs", "https://www.ownbackup.com/open-positions?gh_src=601936b22us", "https://www.pagaya.com/careers-tel-aviv/", "https://jobs.paloaltonetworks.com/job-search-results/?location=Israel&country=IL&radius=25", "https://www.panorays.com/careers/", "https://papayaglobal.com/careers/", "https://paykey.recruiterbox.com/jobs/",
    "https://www.pecan.ai/about-us#jobs", "https://www.peer39.com/careers/","https://www.pendo.io/careers/", "https://www.perion.com/join-us/", "https://persona.ly/about#careers", "https://www.pickapier.com/career-page", "https://company.plarium.com/en/career/", "https://www.playstudios.com/careers/", "https://jobs.plus500.com/",  "https://www.rachip.com/jobs-offers/",
    "https://www.riskified.com/careers/", "https://samsung-careers.co.il/", "https://jobs.sap.com/search/?createNewAlert=false&q=sap+careers+ISRAEL+jobs&locationsearch=israel&optionsFacetsDD_department=&optionsFacetsDD_customfield3=&optionsFacetsDD_country=", "http://www.sarltd.com/", "https://www.scd.co.il/find-a-job/", "https://www.sciplay.com/careers/index.html",
    "https://valid.network/careers/", "https://www.vastdata.com/careers", "https://vectoriousmedtech.com/company/join-us/","https://www.viaccess-orca.com/hr-mini-site-work-with-me", "https://vulcan.io/careers/", "https://www.webpals.com/careers/", "https://waterfall-security.com/company/careers/","https://www.vonage.com/corporate/careers/search/?department=0&office=4010269002",
    "https://jobs.ylventures.com/companies/yl-ventures","https://www.walkme.com/careers/careers_list/?region=emea" ,"https://www.yotpo.com/jobs/", "https://zencity.io/careers/", "https://www.zebra-med.com/careers", "https://www.guardicore.com/company/careers/", "https://www.payoneer.com/careers/"]

    urlsPagination = ["https://www.amazon.jobs/en/search?base_query=&loc_query=israel&type=area&latitude=31.78004&longitude=35.21874&country=ISR","https://jobs.apple.com/en-il/search?location=israel-ISR#&ss=phy%20algo&t=0&so=&lo=0*ISR&pN=0&openJobId=113548234", "https://jobs.qualcomm.com/public/search.xhtml", "https://careers-redhat.icims.com/jobs/search", 
    "https://careers.checkpoint.com/index.php?m=careers&a=jobs&country_code=IL", "https://forcepoint.wd1.myworkdayjobs.com/external-careers/1/refreshFacet/318c8bb6f553100021d223d9780d30be", "https://www.nice.com/careers/find-a-job/?current-page=1", "https://proofpoint.wd5.myworkdayjobs.com/ProofpointCareers", "https://www.servicenow.com/careers.html", 
    "https://careers.hpe.com/jobs", "https://jobs.microfocus.com/global/en/search-results?m=3&location=Israel%20OOH%2C%20Center%20District%2C%20Israel", "https://aluperf.referrals.selectminds.com/jobs/search/24076431", "https://radware.taleo.net/careersection/ex/joblist.ftl", "https://salesforce.wd1.myworkdayjobs.com/External_Career_Site"]
     
    #positions = ["web designer", "ux/ui designer", "ux/ui" , "product designer", "front-end ", "front end ", "fe developer", "frontend " ] 
    #positions = ["ios developer","android developer","front-end ", "front end ", "fe developer", "frontend ", "back-end ", "backend developer", "backend ", "fullstack "] 
    #positions = ["front-end ", "front end ", "fe developer", "frontend "]
    positions = ["Support tier", "support specialist", "support supervisor", "support team lead", "senior support", "support "]
    #positions = ["data scientist", "data analyst", "data engineer", "bi developer", "bi analyst" ] 
    #positions = ["devops", "sre ", "Reliability ","bizops", "bizdevops" ,"dataops"]
    #positions = ["product manager", "technical product manager", "product analyst manager"]
    #positions = ["penetration test", "penetration tester", "risk management", "cyber security", "intelligence analyst", "ethical hacker"]
    for url in urls:
        try:
            response =requests.get(url, headers=headers)
            if response.status_code==200:
                for position in positions:
                    r = response.text.lower().find(position)
                    if r > -1:
                        print("Check the site {} The first position found was {}. Check all anyway.".format(url, position))
                        break
            else:
                print("This site is not working fine: {} , status {}, please check manually".format(url, response.status_code))    
        except: 
            print("An exception occurred in the site {}".format(url)) 

    for url in urlsPagination:
        print("Check this site with pagination: {}".format(url))