��          �               |     }     �     �  �   �  �   n     �  M   �  Y   E     �     �     �     �     �  "     v   *  >   �  �   �  <   �  �   �  �   l  �   Q  Y  7     �	     �	     �	  �   �	  �   �
       K     ]   j     �     �      �          ,  &   >  q   e  T   �  �   ,  H   �  �   C    �  ,  
   Broker configuration Configuration Contents Each time a new reading is parsed, either created by the datalogger or v1/v2 API. You can have each parsed reading passed on to your broker either in JSON format or on a per-field per-topic basis. Each time a telegram is read via the v1 API or datalogger. You can have the entire telegram string passed on to your MQTT broker. Events For example, this will format the JSON message to only contain these fields:: For example, this will make the application only broadcast these fields to their topics:: Integration: MQTT JSON telegram configuration Raw telegram configuration Raw telegrams Reading creation Split topic telegram configuration Support for MQTT is disabled by default in the application. You may enable it in your configuration or admin settings. The application supports sending MQTT messages to your broker. The broker configuration allows you to set the hostname and port of your broker. Optionally, you can enable SSL (if your broker supports it), credentials and the Quality of Service used for MQTT messaging. The following events can trigger MQTT messages when enabled: This allows you to send each raw telegram received to your broker. Just enable it and enter the topic path it should be sent to. This allows you to send each reading created to your broker, in JSON format. You can alter the field names used, by changing their name on the right hand side. You may even remove the lines of the fields you wish to omit at all. This allows you to send each reading created, but splitted in multiple messages. For each field you can designate a separate topic, by changing their path on the right hand side. You can remove the lines of the fields you wish to Project-Id-Version: DSMR Reader 1.x
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2018-10-09 20:07+0200
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: 
Language: nl
Language-Team: 
Plural-Forms: nplurals=2; plural=(n != 1)
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.5.1
 Brokerconfiguratie Configuratie Inhoudsopgave Elke keer dat er een nieuwe meting is opgeslagen, ofwel via de datalogger ofwel via de v1/v2 API. Je kunt elke nieuwe meting doorsturen naar je broker in ofwel JSON-formaat, ofwel los per veld per topic. Elke keer dat een telegram is is uitgelezen via de v1 API of datalogger. Je kunt het gehele telegram 1-op-1 doorsturen naar je MQTT-broker. Events Voorbeeld: Dit zorgt ervoor dat het JSON-bericht alleen deze velden bevat:: Voorbeeld: Dit zorgt ervoor dat de applicatie alleen deze velden doorstuurt naar hun topics:: Integratie: MQTT JSON telegram configuratie Onbewerkte telegram configuratie Onbewerkte telegrammen Meting aangemaakt Gesplitste topic telegram configuratie Ondersteuning voor MQTT is standard uitgeschakeld. Je kunt dit inschakelen in de configuratie/admin-instellingen. De applicatie ondersteunt het versturen van MQTT-berichten naar je eigen broker toe. The broker configuration allows you to set the hostname and port of your broker. Optionally, you can enable SSL (if your broker supports it), credentials and the Quality of Service used for MQTT messaging. De volgende events kunnen MQTT-berichten versturen wanneer ingeschakeld: Dit zorgt ervoor dat elk onbewerkt telegram 1-op-1 wordt doorgestuurd naar je broker. Je hoeft dit alleen in te schakelen en het topic in te voeren waar het naartoe gestuurd mag worden. Dit stelt je in staat om elke aangemaakte meting naar je broker door te sturen, in JSON-formaat. Je hebt invloed op de naamgeving van de velden, door deze aan de rechterzijde aan te passen. Je kunt ook regels weghalen waarvan je de velden uberhaupt niet wenst te zien. Dit stelt je in staat om elke nieuwe meting door te sturen naar je broker, maar in gesplitst formaat over meerdere berichten. Voor elk veld kun je een topic toewijzen waar de waarde naartoe gestuurd kan worden. Verwijder de regels van de velden die je überhaupt niet gebruikt om ze uit te schakelen. 