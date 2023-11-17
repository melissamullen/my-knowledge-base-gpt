# My Knowledge Base

*Note: This is an on-going project. If you have any questions, thoughts, or suggestions, feel free to reach out: melissa.ann.mullen@gmail.com.*

- [Project Overview](#project-overview)
- [Access to Data](#access-to-data)
- [Example Messages to the Knowledge Base](#example-messages-to-the-knowledge-base)
- [Use Cases](#use-cases)
  - [Context-aware Recommendations](#context-aware-recommendations)
  - [Introspection](#introspection)
  - [Memory](#memory)

## Project Overview

The human brain can only hold so much information, and can only synthesize so much data. One of humanity’s greatest leaps forward was the development of writing, because it allowed people to document information externally and reference it later. I hope to build an application that pushes this idea further.

My goal is to build an application connected to an LLM which acts as a repository for everything I know, or have known. The utility of this kind of technology extends beyond just memory assisstance. Such an app would allow for introspection (observing how our beliefs and values have changed over time and conversing about what may have caused these changes). It would allow those who struggle with communication to express their point of view clearly and with the intended audience in mind.

I only wish I'd had this idea sooner, so that I could remember the details of all my college courses. 

Below are some considerations and potential use-cases.

## Access to Data
For the knowledge base to really shine, users should grant access to the following:

- Texts
- Email
- Calendar

Given the extreme sensitivity of that data, on top of all the intimate details the app will collect about the lives of users, security and privacy considerations will be paramount during development. 

## Example Messages to the Knowledge Base
The user can add background data to their knowledge base, filling it in on their past, the people in their lives, their job, etc., at a rate they feel comfortable with. The app could gradually learn about them over time. Alternatively, the user could ask the app to ask questions that will help it better understand the user's life up to this point. This is the suggested approach in order optimize and expedate its utility. Here are some examples of messages one might send to the bot.

- Here's a picture [or link to] of an article in the newspaper I just read
- I just got back from a 3 mile run, and I feel great
- I forget if I already told you, but my roomate's name is Renee. We met when I worked at Joe's restaurant in college for a few summers.
- My parents are going to Cape Cod this weekend so I'm watching their dog, Rosie. Rosie is best friends with my dog Emmy

## Use Cases

If the user sends messages (like the examples above) consistantly, that's when the interesting use cases start to arrise.

### Context-aware Recommendations
- Create a spreadsheet with links to the perfect Christmas gifts for my immediate family and close friends. Provide 3 options for each: `Budget`, `Reasonable`, `Splurge`
- Knowing my mom, how would you suggest I tell her I can't make it to Thanksgiving dinner?
- Make an invitation list for a party at my house next weekend 

### Introspection
- How has my emotional state and general happiness evolved over time? What do the periods of time that I'm doing well all have in common?

### Memory
- What concepts did I learn about in my Thermodynamics class in college?
- What was that helpful blog I found called that explained General Relativity really well?
- What was the name of my favorite teacher in grad school?
- What movies have I seen in the last few years?
- What were my takeaways from the book Guns, Germs, and Steel?
- What news article have I read recently that John would find interesting?
- What was the name of that guy I met at the AI conference last month?
