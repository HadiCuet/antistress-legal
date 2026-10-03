# AntiStress — Privacy Policy

**Effective date:** October 4, 2026

AntiStress is a collection of calm, touchable worlds for iPhone and iPad. It is built to be private: there is no account, no advertising, no analytics and no tracking. This policy explains the little data the app handles, why, and the choices you have.

## 1. Who we are

AntiStress is developed and operated by **Abdullah Al Hadi** ("we", "us"). For the EU / UK / EEA General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA/CPRA), Abdullah Al Hadi is the **data controller** for personal data processed through the app. For any privacy question, write to **mukashi.dev@gmail.com**.

## 2. Data the app handles

### Stays only on your device

The app keeps a few things on your device so it works the way you left it. They are never sent to us. If you use iCloud Backup, Apple includes them in your encrypted backup; that is between you and Apple.

- **Settings:** the world you used last, Sound and Haptics, each world's options, the reminder time and the sleep timer length.
- **Breathe check-ins:** if you rate how tense you feel before and after a Breathe session, those ratings.
- **Pictures of the worlds:** small pictures of each world for the Worlds gallery, kept in the app's cache.
- **App bookkeeping:** which guides you have seen, the days you opened the app, and whether you were already asked for a rating, so the request appears at most once per version.

### Notifications from us (Firebase Cloud Messaging)

**Firebase Cloud Messaging**, a Google service, delivers the app's occasional notifications, such as a note that a new world has arrived.

- **We store no device tokens**, not on your device and not on a server. We have no user database.
- Every message is addressed to a **topic**, not to a person. Your device joins two: one for everyone, and one for the language the app is shown in. That membership tells Google's delivery service the app's language, and nothing else.
- Because we send to topics, **we cannot target an individual person.** Everyone on a topic gets the same message.
- To deliver a notification at all, Google issues a registration token for this installation of the app. It is per-install and resets when the app is reinstalled.
- Notifications are optional; see Section 3.

The daily reminder you can turn on is different: it is scheduled on your device and never involves a server.

## 3. Permissions the app may ask for

Each one is optional:

- **Notifications:** for the daily reminder and the occasional notification from us. You can turn them off at any time in iOS Settings → Notifications → AntiStress.
- **Apple Health (write only):** if you allow it, finished Breathe sessions are saved to Health as Mindful Minutes. AntiStress never reads anything from Health. Health data is handled by Apple under Apple's terms.
- **Photos (add only):** "Save this moment" adds the picture you took to your photo library. The app can't see your existing photos.
- **A photo you pick:** the Bubbles world can take colours from a photo you choose. The photo is read once on your device and is not stored or sent anywhere.

## 4. How we use this data

- **On-device data** powers the app's features: picking up where you left off and applying your settings. It is used for nothing else.
- **Firebase Cloud Messaging** lets us tell people about new worlds and features, in their own language.

We do not sell your personal information, and we do not share it for cross-context behavioral advertising. We do not share data with advertisers, and we do not build profiles across other apps.

## 5. Children

AntiStress is suitable for everyone. It has no accounts and asks for no personal information. The only data that leaves the device is the notification topic membership described above, which identifies no one.

## 6. Third parties

Apart from Apple, the only service the app communicates with is **Firebase Cloud Messaging**, operated by Google LLC. Google processes this data as our service provider, under the [Firebase Data Processing and Security Terms](https://firebase.google.com/terms/data-processing-terms). Google's own practices are covered by the [Google Privacy Policy](https://policies.google.com/privacy). Notifications reach your device through **Apple Push Notification service**, operated by Apple. Siri, Shortcuts, widgets and Apple Health are Apple features, covered by [Apple's Privacy Policy](https://www.apple.com/legal/privacy/). When you tap Rate or Share in the app's Settings, the app asks Apple's App Store for the address of its own page; the request carries no personal data.

Google primarily processes this data on servers in the **United States**. For users in the EEA, UK or Switzerland, transfers rely on Google's Data Processing and Security Terms, which incorporate the European Commission's Standard Contractual Clauses and the UK International Data Transfer Addendum.

No analytics, advertising or tracking SDK is included in the app.

## 7. How long we keep it

- **On your device:** until you delete the app, which removes everything it stored.
- **Notification topic membership:** for as long as the app is installed with notifications allowed; Google removes inactive registrations over time.

## 8. Your rights and choices

You can turn off notifications, Health saving and Sound at any time, in the app's Settings or in iOS Settings. Because we hold no personal data about you, there is nothing for us to export or delete; deleting the app removes everything on your device. Depending on where you live, you may have rights to access, correct or delete personal data and to object to processing; write to us and we will help.

## 9. Security

The app keeps its data in the iOS app sandbox. Communication with Firebase is encrypted in transit.

## 10. Changes to this policy

If this policy changes, the new version will replace this page at **https://hadicuet.github.io/antistress-legal/** and the effective date above will be updated. Material changes will be called out in the app's release notes.

## 11. Contact us

Questions, requests or complaints: **mukashi.dev@gmail.com**.
