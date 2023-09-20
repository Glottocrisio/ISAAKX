from mediawikiapi import MediaWikiAPI

mediawikiapi = MediaWikiAPI()
print(mediawikiapi.summary("Wikipedia"))

mediawikiapi.search("Alexander the Great")

obj = mediawikiapi.page("Alexander the Great")
obj.title

obj.url

obj.content

obj.links[0]


mediawikiapi.config.language = "it"
mediawikiapi.summary("", sentences=1)

#clickstreamdata