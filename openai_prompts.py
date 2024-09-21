CHARACTER_DEVELOPMENT = """
We define character development in terms of changes that a character undergoes through the course of narrative events. 

We define changes broadly to include cognitive, emotional, behavioral, spiritual, moral, bodily, and social changes. 

Notably, we do not consider environmental changes for characters sufficient for character development, but acknowledge that other types of change (e.g. emotional, social) often accompany or are caused by environmental changes.

Rate the narrator’s character development based on the following scale:
1 - no change
2 - limited change
3 - moderate change
4 - significant change
5 - life-altering, dramatic change

Examples:
- I watched the birds splashing in the puddle from a bench at the park. They were so playful and content, even as it started to drizzle. (1 - character does not change)
- It wasn’t until my brother told me what he’s been going through that I realized how distant I had been. I broke down in front of him at the time. From that day forward, I decided to be there for my family, no matter what–even if that meant quitting my job and moving home. (5 - multiple dramatic changes)

Respond with a single integer.

Story: [STORY]
"""

VULNERABILITY = """
Rate how emotionally vulnerable the narrator is in telling their story. We define vulnerability as how personal or intimate the information shared by the narrator is.

Use the following scale:
1 - not vulnerable at all
2 - somewhat vulnerable
3 - very vulnerable

Examples:
- But I just doubt myself a lot. It's inevitable. (3 - the author reveals their self doubt)
- I went on a very memorable trip to Crater Lake Oregon on July 8th. (1 - does not share any sensitive information)

Respond with a single integer.

Story: [STORY]
"""

OPTIMISM = """
Rate the level of optimistic/pessimistic tone in the narrator’s story. This should be the tone from the narrator’s perspective, not of other characters in the story.
 
-2 - very pessimistic
-1 - somewhat pessimistic
0 - neutral
1 - somewhat optimistic
2 - very optimistic

Examples:
- I feel alone. It is so frustrating. I used to be fine with it, but then for some reason I actually started wanting to have a friend. I have nobody. And nobody around me seems interesting enough to me. Life gets boring. And frustrating. (rating = -2, very pessimistic)
- He is grown up and I have done my job to get him out into the world. I will miss his teenage years (somewhat), but I am proud of him. (rating = 2, very optimistic)

Respond with a single integer.

Story: [STORY]
"""

EMOTIONAL_METAPHORS_IMAGERY = """
Rate the vividness of emotions described in the story. For example, vividness can be characterized by metaphor, simile, imagery, or strong language.

Use the following scale:
1 - not vivid at all
2 - somewhat vivid
3 - very vivid

Examples:
I didn’t feel great about the situation. (1)
He was a hard-hitter in business, but outside of work he was completely different. (2)
The pain of losing someone is like being stabbed in the chest. I was devasted when I lost her. (3)
I was totally exhausted, tears running down my face (3).

Respond with a single integer.

Story: [STORY]
"""

COGNITION = """
Rate how prominent descriptions of cognitive processes are in the story. We define descriptions of cognitive processes as statements that reveal the mental state or thinking pattern of the narrator.

Use the following scale:
1 - minimal or no cognitive processes
2 - moderate prominence of cognitive processes
3 - high prominence of cognitive processes

Examples:
- I was born in the United States. (rating = 1)
- I wondered if I had seen him before. (rating = 2)
- I was thinking about how I could do it but I couldn’t focus because I kept remembering what Sam said to me yesterday. (rating = 3)

Respond with a single integer.

Story: [STORY]
"""

EVALUATIONS_ATTRIBUTIONS_BELIEFS_DESIRES = """
Rate the degree to which the narrator expresses an evaluation, attribution, belief, or desire.

Use the following scale:
1 - none
2 - limited to moderate 
3 - prominent

Examples:
My friends go to concerts once a month or so. (1)
I think he quit his job because of salary concerns (2 - uncertainty surrounding attribution)
It is a terrible place to work because they never let you use your vacation time. (3 - shows author’s negative evaluation of an employer)
The table setting was a big bouquet of purple flowers. Awfully old-fashioned. (3 - shows author’s belief that bouquets of purple flowers to be old-fashioned)
I used to have a lovely garden, but my neighbor’s dog trampled the flowers one day and they never recovered. (3 - shows that author attributes loss of garden to dog)
I wanted nothing more to be accepted to my dream college. (3 - show’s desire for college acceptance)

Respond with a single integer. Do not include any words or punctuation marks in your answer.

Story: [STORY]
"""

BODY_PERCEPTION = """
Rate the vividness of the narrator’s perception or bodily sensations described in the story. For example, vividness can be characterized by metaphor, simile, imagery, or strong language. 

Focus on physical sensations, not emotional states.

Use the following scale:
1 - not vivid at all
2 - somewhat vivid
3 - very vivid


Examples:
I drove for seven hours that day. Unfortunately, it rained for the first 5 hours of the trip. (1)
I have a pinched nerve in my back which makes certain yard work somewhat painful. (2)
The rock prodded my foot, poking the sole of my shoe, making it painful for me to walk. (3)
The cold water hit my face. (3)

Respond with a single integer.

Story: [STORY]
"""

ACTION_VERBS = """
An action verb is simply a verb that represents action. 

Examples of action verbs:
- run 
- smile
- made
- said
- drove

Not all verbs are action verbs, such as stative verbs (e.g. “have”, “resemble”, “want”).

Count the number of action verbs in the story. 

Respond with a single integer. Do not include any words or punctuation marks in your answer.

Story: [STORY]
"""

TEMPORAL = """
Rate the extent to which the character focuses on the past (such as expressing nostalgia or reflections on memories) vs on the future (anticipation, looking forward) in the context of the story. 

Note that we are not asking whether the story is a past-tense, present-tense, or future-tense story. We are concerned with the orientation the narrator has toward the past, present, or future. We define ‘extent’ as the amount of narration time oriented toward the relative past, present, or future. 

Use the following scale:
-2 - heavy focus on the past
-1 - light focus on the past
0 - focus on the present
1 - light focus on the future
2 - heavy focus on the future

Examples:
- “I was stuck in bureaucratic processes for a year, and the whole time I was dreaming of the day my application processing was complete.” (2) 
- “I went to the mall and saw a parade on my way.” (0)
- “When I started taking my test, I regretted how little I had studied.” (-1)

Respond with a single integer

Story: [STORY]
"""

PLOT_TRAJECTORY = """
Stories are structured by a sequence of events.

We define plot trajectory as the amount and significance of events in the story. 

If the events are banal or insignificant and do not have a big impact on characters, then the plot trajectory is relatively small. If the events significantly impact characters or setting, then the story has a large plot trajectory. 

Rate the degree to which characters and setting are transformed through the course of the story based on the following scale:
1 - no change
2 - trivial change
3 - moderate change
4 - significant change
5 - life-altering, dramatic change

Examples:
I stared out the window absent-mindedly for three hours. It was a lovely day. (1)
I heard a crash outside. I ran outside to see what had happened. It turned out the wind had blown over a box of garden tools. (3)
After a long and difficult pregnancy, I gave birth to a beautiful baby at 4:15pm. It was a crazy day at the hospital, but thanks to my family and the medical staff, we got through it! (5)

Respond with a single integer.

Story: [STORY]
"""

EMOTION_SHIFTS = """
Most (but not all) emotions have either a positive (high) or negative (low) valence.  

For example, “anger” and “disgust” are low valence, whereas “happy” and “content” are high valence. 

Other emotions like “ambivalent” or “surprised” could be neutral, low, high, or ambiguous depending on the context.

We consider 5 different types of emotional shifts that can occur in a story:
- low-to-high valence (e.g. sad to happy)
- high-to-low valence (e.g. happy to sad)
- high-to-high valence (e.g. happy to hopeful)
- low-to-low valence (e.g. sad to angry)
- ambiguous-to-any valence (e.g. bittersweet to excited)

We are interested in relatively straightforward emotion shifts that are either explicitly asserted in the text or easily inferrable based on information in the text. We are less interested in extremely subtle emotional shifts (e.g. joyful to content).

Rate the degree of emotional shifts in the story below.

Use the following scale:
1 - no emotional shifts
2 - limited or trivial emotional shifts
3 - moderate emotional shifts
4 - significant emotional shifts
5 - life-altering, dramatic emotional shifts

Example Story:
- “I went to college for 1 year before dropping out.” (1)
- “I was surprised to see my friend show up at the cafe where I was working” (2)
- “I was frustrated with Ben for not inviting me, but when I ran into him a few weeks later, our conversation went fine.” (3)
- “I worked hard all semester and was mentally and physically exhausted by the end. It was such a relief to see my grades come in and see that all of my hard work paid off.” (4)
- “I was so excited to get out of class but before the bell rang the principal called me to his office. I was in trouble. I was stressed out of my mind walking to his office, but when I got there, he gave me the good news: I won the school-wide design contest!” (5)

Respond with a single integer. 

Story: [STORY]
"""

RESOLUTION = """
In the course of events and interactions between characters, stories introduce conflict. Stories also raise questions about the motives of characters, the meaning of events, and more. Conflict can be explicitly or implicitly referenced by narrators. Alternatively, the reader may subjectively perceive conflict in the situations described by narrators.

Resolution refers to the extent to which conflict is addressed and questions are answered by the end of the story. There are many ways a story may be resolved, partially or completely. Resolution can occur for the narrator, characters within the story, or the reader.

A story with low resolution may not have much conflict or leave conflict unaddressed by the end of the story. A story with high resolution will involve conflict that is addressed or raise questions that are ultimately answered. 

Rate the degree of resolution by the end of the story based on the following scale: 
1 - no resolution
2 - limited resolution
3 - moderate resolution
4 - significant resolution
5 - complete resolution

Examples:
I couldn’t believe that he didn’t apologize. How can someone just pretend that nothing happened? (1)
I was homeless and finally found a new job, but I hate it and want to find a new one. (3)
I looked for love my entire life, and had almost given up, when I met them. Now I couldn’t be more in love. (5)

Respond with a single integer. Do not include any words or punctuation marks in your answer.

Story: [STORY]
"""

SETTING = """
Rate the vividness of the setting described in the story. For example, vividness can be characterized by metaphor, simile, imagery, or strong language.

Examples:
I went to the restaurant to grab a bite to eat. (1)
The sun cast warm rays onto the concrete in the park. (3)
The waves in Palos Verdes crashed against the shore, making beautiful ribbons (3)
There was a house, with music playing in it (2)

1 - not vivid at all
2 - somewhat vivid
3 - very vivid

Story: [STORY]
"""



















CHARACTER_DEVELOPMENT_NO_CB = """
Rate the narrator’s character development in the story based on the following scale:
1 - no change
2 - limited change
3 - moderate change
4 - significant change
5 - life-altering, dramatic change

Respond with a single integer.

Story: [STORY]
"""

VULNERABILITY_NO_CB = """
Rate the narrator's emotional vulnerability in the story based on the following scale:
1 - not vulnerable at all
2 - somewhat vulnerable
3 - very vulnerable

Respond with a single integer.

Story: [STORY]
"""

OPTIMISM_NO_CB = """
Rate the narrator's tone in the story based on the following scale:
-2 - very pessimistic
-1 - somewhat pessimistic
0 - neutral
1 - somewhat optimistic
2 - very optimistic

Respond with a single integer.

Story: [STORY]
"""

EMOTIONAL_METAPHORS_IMAGERY_NO_CB = """
Rate the vividness of emotions in the story based on the following scale:
1 - not vivid at all
2 - somewhat vivid
3 - very vivid

Respond with a single integer.

Story: [STORY]
"""

COGNITION_NO_CB = """
Rate the prominence of cognitive processes in the story based on the following scale:
1 - minimal or no cognitive processes
2 - moderate prominence of cognitive processes
3 - high prominence of cognitive processes

Respond with a single integer.

Story: [STORY]
"""

EVALUATIONS_ATTRIBUTIONS_BELIEFS_DESIRES_NO_CB = """
Rate the degree to which the narrator expresses an evaluation, attribution, belief, or desire in the story based on the following scale:
1 - none
2 - limited to moderate 
3 - prominent

Respond with a single integer. Do not include any words or punctuation marks in your answer.

Story: [STORY]
"""

BODY_PERCEPTION_NO_CB = """
Rate the vividness of the narrator's perception or bodily sensations in the story based on the following scale:
1 - not vivid at all
2 - somewhat vivid
3 - very vivid

Respond with a single integer.

Story: [STORY]
"""


TEMPORAL_NO_CB = """
Rate the extent to which the character focuses on the past vs on the future in the story based on the following scale:
-2 - heavy focus on the past
-1 - light focus on the past
0 - focus on the present
1 - light focus on the future
2 - heavy focus on the future

Respond with a single integer.

Story: [STORY]
"""

PLOT_TRAJECTORY_NO_CB = """
Rate the amount of plot in the story based on the following scale:
1 - no plot
2 - trivial plot
3 - moderate plot
4 - significant plot
5 - life-altering, dramatic plot

Respond with a single integer.

Story: [STORY]
"""

EMOTION_SHIFTS_NO_CB = """
Rate the degree of emotional shifts in the story based on the following scale:
1 - no emotional shifts
2 - limited or trivial emotional shifts
3 - moderate emotional shifts
4 - significant emotional shifts
5 - life-altering, dramatic emotional shifts

Respond with a single integer. 

Story: [STORY]
"""

RESOLUTION_NO_CB = """
Rate the degree of resolution in the story based on the following scale: 
1 - no resolution
2 - limited resolution
3 - moderate resolution
4 - significant resolution
5 - complete resolution

Respond with a single integer. Do not include any words or punctuation marks in your answer.

Story: [STORY]
"""

SETTING_NO_CB = """
Rate the vividness of the setting in the story based on the following scale:
1 - not vivid at all
2 - somewhat vivid
3 - very vivid

Respond with a single integer. 

Story: [STORY]
"""