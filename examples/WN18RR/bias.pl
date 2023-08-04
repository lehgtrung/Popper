max_clauses(10).
enable_recursion.
head_pred(derivationallyRelatedForm,2).
body_pred(instanceHypernym,2).
body_pred(hypernym,2).
body_pred(alsoSee,2).
body_pred(memberMeronym,2).
body_pred(synsetDomainTopicOf,2).
body_pred(hasPart,2).
body_pred(memberOfDomainUsage,2).
body_pred(memberOfDomainRegion,2).
body_pred(verbGroup,2).
body_pred(similarTo,2).
:- discontiguous instanceHypernym/2.
:- discontiguous hypernym/2.
:- discontiguous alsoSee/2.
:- discontiguous memberMeronym/2.
:- discontiguous synsetDomainTopicOf/2.
:- discontiguous hasPart/2.
:- discontiguous memberOfDomainUsage/2.
:- discontiguous memberOfDomainRegion/2.
:- discontiguous verbGroup/2.
:- discontiguous similarTo/2.
