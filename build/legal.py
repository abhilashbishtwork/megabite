"""Generates privacy.html, terms.html, refund.html. Edit CONTENT, run: python3 build/legal.py"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATED = "11 November 2026"
ENTITY = "Curefoods India Private Limited"
EMAIL = "megabite@curefoods.in"; PHONE = "8792539301"
ADDR = "72/4, Hosur Road, Bengaluru 560068"
IOS = "https://apps.apple.com/in/app/megabite-online-ordering/id6817365667"
AND = "https://play.google.com/store/apps/details?id=com.app.uengage.megabite"

PAGES = {
"privacy": ("Privacy Policy", "How we collect, use and protect your information.", [
 ("", [f"MegaBite is a brand of {ENTITY} (“MegaBite”, “we”, “us”, “our”). This Privacy Policy explains how we handle your information when you visit this website or use the MegaBite app (together, the “Services”). It is published in accordance with the Information Technology Act, 2000, the Information Technology (Reasonable Security Practices and Procedures and Sensitive Personal Data or Information) Rules, 2011, and the Digital Personal Data Protection Act, 2023.",
       "By using the Services you agree to this Policy. If you do not agree, please do not use the Services."]),
 ("Information we collect", ["When you use the MegaBite app we collect only what we need to take and deliver your order:",
   ["Your name and mobile number, used to create and verify your account.",
    "Delivery address and, if you allow it, your device location, used to find your nearest kitchen and deliver your order.",
    "Email address, date of birth and anniversary, only if you choose to share them.",
    "Order history, preferences and support conversations.",
    "Basic device and usage information such as device type, app version, IP address and crash logs."],
   "Payments are processed by licensed payment gateways. We do not store your full card, UPI or net-banking credentials.",
   "This website itself does not ask you for any personal information."]),
 ("How we use it", [["Verify your account and process, prepare and deliver your orders.",
    "Send order status updates by SMS, WhatsApp, call or app notification.",
    "Provide customer support and resolve refunds or complaints.",
    "Share offers and birthday or anniversary treats, which you can opt out of at any time.",
    "Improve our menu, app and service, and prevent fraud or misuse."]]),
 ("Sharing", ["We never sell your personal information. We share it only:",
   ["With our group companies, delivery partners, payment gateways and technology providers (including our ordering platform provider, which hosts account data on secure servers) strictly to run the Services, under confidentiality obligations.",
    "When required by law, court order or a government authority, or to prevent fraud, cyber incidents or other offences."]]),
 ("Cookies", ["This website may use basic cookies and analytics to understand traffic and improve the site. Cookies cannot read data from your device and you can disable them in your browser settings."]),
 ("Data security & retention", ["We use reasonable security practices, including encryption, access controls and firewalled servers, to protect your information. No system is completely secure, but we work to keep your data safe and retain it only as long as needed for the purposes above or as required by law."]),
 ("Your choices", ["You can access or update your profile in the app, opt out of promotional messages, or ask us to delete your account by writing to "+EMAIL+"."]),
 ("Changes", ["We may update this Policy from time to time. The latest version will always be on this page with the date it was last updated."]),
 ("Grievance officer", [f"For any questions, complaints or concerns about your data, contact our Grievance Officer at <a href=\"mailto:{EMAIL}\">{EMAIL}</a> or {PHONE}. Address: {ADDR}."]),
]),
"terms": ("Terms & Conditions", "The rules for using the MegaBite website and app.", [
 ("", [f"These Terms govern your use of this website and the MegaBite app (the “Services”), operated by {ENTITY} under the MegaBite brand (“MegaBite”, “we”, “us”). By using the Services you agree to these Terms. If you do not agree, please do not use them."]),
 ("Ordering", ["Orders can be placed only through the MegaBite app, available on the App Store and Google Play. This website is for information only and does not accept orders.",
   ["Menu items, prices, offers and delivery areas may change and depend on your location and kitchen availability.",
    "Prices shown in the app at checkout are final. MegaBite does not charge delivery or platform fees unless clearly shown in the app.",
    "Please check allergen and dietary information in the app before ordering. Our kitchens handle common allergens.",
    "Cancellations and refunds are covered by our <a href=\"refund.html\">Refund Policy</a>."]]),
 ("Your account", ["You are responsible for keeping your account and mobile number secure and for all activity on your account. Please give accurate details, especially your delivery address."]),
 ("Use of content", ["All logos, brand names, images, text and designs on the Services are owned by or licensed to MegaBite and its group companies. You may not copy, sell, modify or use them for any public or commercial purpose without written permission."]),
 ("Acceptable use", ["You must not:",
   ["Access data or accounts you are not authorised to use, or try to probe, scan or breach the security of the Services.",
    "Interfere with the Services, for example through viruses, overloading or flooding.",
    "Misuse offers or referral codes, place fraudulent orders, or abuse delivery partners or staff.",
    "Use the Services for anything unlawful, infringing, defamatory, obscene or abusive."],
   "We may suspend or close accounts that break these rules and may involve law enforcement where needed."]),
 ("Liability", ["To the extent permitted by law, MegaBite and its group companies, directors and employees are not liable for indirect, incidental or consequential losses arising from your use of, or inability to use, the Services. Our total liability for any claim is limited to the amount you paid for the order concerned."]),
 ("Indemnity", ["You agree to indemnify MegaBite, its officers, directors, employees and agents against claims arising from your misuse of the Services or breach of these Terms."]),
 ("Changes & governing law", [f"We may revise these Terms at any time by updating this page. These Terms are governed by the laws of India, and courts in Bengaluru have exclusive jurisdiction. Questions: <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
]),
"refund": ("Refund Policy", "Cancellations, failed payments and refunds for MegaBite orders.", [
 ("", ["This policy applies to orders placed on the MegaBite app."]),
 ("Your money is safe", ["If money was deducted from your UPI, card, net-banking or wallet but your order wasn't confirmed, don't worry. It is protected under consumer safeguarding guidelines and will be either processed or refunded."]),
 ("Cancellations", ["We start cooking as soon as your order is confirmed and dispatch a delivery partner right away, so <strong>orders cannot be cancelled once placed</strong>. Please double-check your items and address before you pay.",
   "In exceptional cases, such as an item being unavailable or an unforeseen emergency at our end, we may cancel the order and refund you in full. Other exceptions are reviewed case by case and are not guaranteed."]),
 ("Failed or pending payments", [["This usually happens when the bank can't confirm the payment immediately.",
    "If the bank confirms within 15 minutes, your order is processed automatically.",
    "If the bank confirms after 15 minutes, the order is rejected and a refund is started automatically."]]),
 ("Missing, wrong or damaged items", ["If something is missing, incorrect or not up to the mark, raise it from the order in the app's Help section or write to us within 24 hours with your order ID and a photo. Approved refunds go back to your original payment method."]),
 ("Refund timelines", ["Once a refund is started, it usually takes <strong>5–7 working days</strong> to reach your account, depending on your bank."]),
 ("Need help?", [f"Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> or call {PHONE}."]),
]),
}

def render(blocks):
    out=[]
    for b in blocks:
        if isinstance(b,list): out.append("<ul>"+"".join(f"<li>{x}</li>" for x in b)+"</ul>")
        else: out.append(f"<p>{b}</p>")
    return "".join(out)

TPL = open(os.path.join(ROOT,"build","legal_tpl.html")).read()
for slug,(title,lede,secs) in PAGES.items():
    body=""; toc=""
    for i,(h,blocks) in enumerate(secs):
        sid=f"s{i}"
        if h: body+=f'<section id="{sid}"><h2>{h}</h2>{render(blocks)}</section>'; toc+=f'<a href="#{sid}">{h}</a>'
        else: body+=f'<section class="intro">{render(blocks)}</section>'
    nav="".join(f'<a href="{s}.html"{" class=on" if s==slug else ""}>{t}</a>' for s,(t,_,_) in PAGES.items())
    page=(TPL.replace("{{TITLE}}",title).replace("{{LEDE}}",lede).replace("{{UPDATED}}",UPDATED)
          .replace("{{BODY}}",body).replace("{{TOC}}",toc).replace("{{TABS}}",nav)
          .replace("{{IOS}}",IOS).replace("{{AND}}",AND).replace("{{EMAIL}}",EMAIL).replace("{{ADDR}}",ADDR))
    open(os.path.join(ROOT,slug+".html"),"w").write(page); print("wrote",slug)
