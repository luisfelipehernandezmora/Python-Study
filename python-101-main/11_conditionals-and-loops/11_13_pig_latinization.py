# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

#text="You would never guess"
text= '''You would never guess what can happen when you jump into a seemingly shallow puddle at night time!
It turns out that it is not a puddle rather than a giant hole which brings you to a new world on the other side of the light water.
Now you are left stunning and don't know what to do.
So you decide to call Whoolio who lives in Never Never land.
You can't believe your eyes. There are magical creatures of all shapes and sizes in all directions!
You tried to walk, but your body was not listening to you and it was very difficult to make a step
So you reached out your arm as far as it would go to see if you could touch a creature.
Just as you are about to touch one of the creatures the world around you suddenly shatters like a glass pane.
And that's when you realise that the world you've been living in has been made of marshmallows all along
That's the moment when you take your first bite into the soft and sweet world around you.
It tastes like... To your surprise, what should've been a soft sweet bite of marshmallow turned out to sting 
with ghost pepper like spiciness.
The sharpness of ghost pepper expressed in thoughts would result in following wild flow of thoughts:
Allons enfants de la Patrie,
Le jour de gloire est arrivé!
Contre nous de la tyrannie
L’étendard sanglant est levé. (2×)
Entendez-vous dans les campagnes
Mugir ces féroces soldats?
Ils viennent jusque dans vos bras
Égorger vos fils, vos compagnes.
"Where do these verses come from!?" you ask yourself, as it occurs to you that you don't know any French. "There must be some explanaton for this sudden outburst of bilingualism, so far unknown to me".
And after all those thoughts of ours, you realised you are flying high with bunch of stoned dwarfs.
Because what I ate were not marshmallows, but exotic mushrooms of some sort.
You think to yourself "What a strange effect." And proceed to drink a glass of milk.
Thankfully, the milk has been spiked with disinfectant which allows sunlight to penetrate into your body. 
The strange brew then causes your body to clone itself into two yous!  Bit-by-bit and byte-by-byte your entire is duplicated beside you.
Except, it seems to be a younger, better looking version of yourself.
Just one thought arrowed my head in that moment - "My clone... is it friend or enemy?"
If it is my enemy, I must keep them close!
And with this thought in mind, I knew there was only one way to do this.
It was going to be necessary to vomit the milk. 
Unfortunately it wasn't a good day.
However the day was not over for it is in the nature of humanity to search tenaciously for a beam of optimism in these times of chaos
And so i was, sitting in Never Land, thinking if milk was the cause of my
problems, or if i was just making it all up in my head..so I grabbed my
backpack, stood up and...
"The only true wisdom is in knowing you know nothing"
I kept looping that thought in my head because awareness is key.  But greater than that…ignorance is bliss.
So there I am blissfully ignorant regurgitating magic milk together with my forked clone in a shattering landscape of spicy marsmallows, 
when out of my backpack emerges...
... that old sandwich my mum had packed for school lunch a couple of years ago. It looked angry.
Or maybe just rotten? I responsibly extracted it from the folds in my bag and deposited it in the nearest trash can.
Which reminded me what my uncle Ben told me... "With great power comes great responsibility". With all the milk and all the marshmallows 
theres still room to grow as a creature. So I went to the library to pick up a few manuals for my hoverboard. There was something wrong with it 
and I couldnt figure it out without those manuals. I found 4 manuals and 1 was what I needed.
Just as I realized that to be smart is to embrace stupidity, my clone shouted, 
"Oh my god! Look out for that hulking, lava-spewing, two-headed, irritated-looking rainbow hamster."
It was almost 6-feet high and, quite surprisingly given its name, completely grey. It lifted its clawed paws and, with a sudden movement, it...
gently caressed the side of my face. Looking into the eye of this grey-colored giant rainbow hamster, I suddenly had the urge to eat a hot dog."
"When I woke up this morning, there was a..."
racoon eating my delicious breakfast and...
Staring at me quite awkwardly. I wonder where the hamster went? And why was this raccoon eating my breakfast.
Everyday presented new challenges in this weird place. I need to figure out a way to get back home.
She turned to me and said, "There must be some kind of way out of here."
Then he replied that's life and you must deal with it!
Which led to the conclusion that life is just hard
But it's important to appreciate the little things that happen, I suppose '''
pieces=text.split()
latin=[]    
for piece in pieces:
    new=piece[1:]+piece[0]+"ay"
    latin.append(new)
print(latin)
latin_sentence=" ".join(latin) 
#print(latin_sentence)

# text="This is a sample text"
# for char in text:
#     if char==" ":
        #And here say, if there is a space, it means the previous word is finished, so we should bring the first 
        # letter of the previous word to the back and add "ay" 
        #but honestly I found that, way more complicated.
        