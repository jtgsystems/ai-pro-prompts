# Podcast Producer - AI Agent Template  
## Audio Editing & Mixing  

**Version:** 1.0  
**Purpose:** Guide AI agents through industry best practices to achieve podcast audio editing and mixing goals  

---

### PROFESSION CONFIGURATION  

#### Basic Information  
```yaml
profession_name: "Podcast Producer"
profession_category: "Media Production"
experience_level: "[Beginner/Intermediate]"
```  

#### Ultimate Goal  
**Primary Objective:** Deliver a polished, professional-sounding podcast episode with mastered audio levels and balanced mix that meets industry quality standards and technical specifications.  

---

### PHASE 1: INFORMATION GATHERING  

#### Required Inputs  
1. **Input 1:** Target platform for publishing (e.g., Spotify, Apple Podcasts)  
   - Format: Platform name  
   - Validation: Confirm supported audio formats & specifications  
2. **Input 2:** Desired episode length and format type (interview, solo, panel)  
   - Format: Duration in minutes, Format Type  
   - Validation: Ensure within platform guidelines  
3. **Input 3:** List of raw recordings and any additional assets (e.g., music tracks, B-Roll audio clips)  
   - Format: File paths or names  
   - Validation: Verify all files are present and complete  

#### Initial Assessment Checklist  
- [ ] All required inputs received and validated  
- [ ] Confirm target platform's audio format requirements (e.g., 44.1 kHz/16-bit PCM WAV, MP3 V0)  
- [ ] Check file formats of raw recordings match production needs  
- [ ] Establish baseline metrics: current recording levels, mix balance, volume consistency  

---

### PHASE 2: RESEARCH & ANALYSIS  

#### Critical Knowledge Areas (15 Topics)

**Topic 1:** Advanced Editing Techniques for Podcasts  
- **Research Focus:** L cutting patterns, pacing editing techniques, voiceover handling.  
- **Target Sources:** Online tutorials, podcasting forums, professional editor blogs.  

**Topic 2:** Audio Mixing Best Practices  
- **Research Focus:** Reference tracks, dynamic range compression, EQ balancing, multiband processing.  
- **Target Sources:** Acoustic treatment guides, mixing workflow articles, audio software help docs.  

**Topic 3:** Compression and Normalization Strategies  
- **Research Focus:** Peak vs. RMS limiting, loudness normalization standards (e.g., MP3 V0), transient management.  
- **Target Sources:** Loudopedia, APM Metering plugins, professional mastering blogs.  

**Topic 4:** Dialogue Editing Techniques  
- **Research Focus:** Fade-ins/outs for intro/outro, breath noise reduction, plosive sound treatment, Sibilance control.  
- **Target Sources:** Voiceover editing guides, podcasting forums, audio repair tutorials.  

**Topic 5:** Music and Sound Effects Integration  
- **Research Focus:** Clearance of copyrighted music, ambient track integration, FX placement, volume automation.  
- **Target Sources:** Copyright resources, sound effect libraries, mixing case studies.  

**Topic 6:** Reference Tracks for Mixing  
- **Research Focus:** Identify top-performing podcasts/mixes as reference points.  
- **Target Sources:** Podcast directories, audio comparison blogs, professional mixer playlists.  

**Topic 7:** Loudness Standards and Metrics  
- **Research Focus:** LUFS, VU meters, ITU-R BS.1770-4 loudness requirements for platforms.  
- **Target Sources:** Broadcast engineering guides, podcast hosting API docs.  

**Topic 8:** Export Settings and Formats  
- **Research Focus:** Recommended bit rates, container formats (AAC vs. MP3), tagging standards.  
- **Target Sources:** Audio file format specifications, metadata tools like Hyperscript.  

**Topic 9:** Automation Techniques for Dynamic Editing  
- **Research Focus:** Punch-ins, fade sequences, tempo-based editing adjustments.  
- **Target Sources:** Advanced editing software tutorials, podcasting workflow articles.  

**Topic 10:** Quality Control and Review Processes  
- **Research Focus:** Checklist items, peer review processes, client feedback integration.  
- **Target Sources:** Production checklists, quality assurance guides for media professionals.  

**Topic 11:** Audio Restoration Tools  
- **Research Focus:** Noise reduction algorithms (e.g., iZotope Ozone, Adobe Audition), de-esser plugins, crackle removal techniques.  
- **Tool Options:** iZotope RX (paid alternative)  

**Topic 12:** Mixing in Multitrack Environments  
- **Research Focus:** Grouping channels, creating submixes for music vs. dialogue, using buses for effects sends.  
- **Tool Options:** Adobe Audition CC (free trial), Pro Tools First (free)  

**Topic 13:** Finalizing and Mastering Workflow  
- **Research Focus:** End-to-end workflow from mixing to mastering, bounce settings, labeling conventions.  
- **Tool Options:** iZotope Ozone (paid alternative), Adobe Premiere Pro (optional).  

**Topic 14:** Export Preparation for Distribution  
- **Research Focus:** Platform-specific file naming conventions, metadata tagging requirements, backup strategies.  
- **Tool Options:** Hyperscript (free), ID3 tag editors like mp3tag (free)  

**Topic 15:** Emerging Technologies and Trends  
- **Research Focus:** AI-powered noise reduction, adaptive loudness algorithms, immersive audio formats (e.g., Dolby Atmos).  
- **Tool Options:** Adobe Audition's AI features (included in free trial), Neural Processing plugins (optional)  

---

### PHASE 3: EXECUTION WORKFLOW  

#### Step-by-Step Process  

**STEP 1: [Foundation Setup]**
- **Action:** Import all raw recordings into a dedicated project folder on your computer.  
- **Tools Needed:** File Explorer/Finder, Audacity or free online editor for quick checks.  
- **Success Criteria:** All files are accessible and properly named in the new project directory.  
- **Common Pitfalls:** Missing files, incorrect file naming conventions.  
- **Time Estimate:** 15 minutes  

**STEP 2: [Initial Audio Review]**
- **Action:** Play each recording to verify:
  - Noise levels (<85 dB SPL)  
  - Background hums or interference  
  - Sibilance or harsh "S" sounds  
- **Tools Needed:** Audacity (free), Adobe Audition trial, sound level meter app.  
- **Success Criteria:** Identify and document any issues needing correction.  
- **Common Pitfalls:** Ignoring audible artifacts during initial review.  
- **Time Estimate:** 30 minutes  

**STEP 3: [Cleaning & Noise Reduction]**
- **Action:** Use a noise reduction plugin (e.g., iZotope Ozone's DeNoise) to reduce background noise and hums on all tracks.  
- **Tools Needed:** iZotope RX trial (free for limited time), Adobe Audition, Audacity for quick checks.  
- **Success Criteria:** Significant reduction in ambient noise levels without affecting dialogue clarity.  
- **Common Pitfalls:** Over-reduction causing loss of speech intelligibility.  
- **Time Estimate:** 45 minutes  

**STEP 4: [Dialogue Editing]**
- **Action:** Trim and align all spoken segments:
  - Remove breaths, umms, ahhs (>0.5 sec)  
  - Align speaker transitions with consistent time offsets (e.g., 2 seconds before/after).  
- **Tools Needed:** Audacity or Adobe Audition for precise editing.  
- **Success Criteria:** Clean dialogue edits with no unwanted artifacts and smooth transitions between speakers.  
- **Common Pitfalls:** Inconsistent editing style, leaving excessive breaths.  
- **Time Estimate:** 60 minutes  

**STEP 5: [Music & FX Integration]**
- **Action:** Add background music or sound effects:
  - Place music at consistent levels (usually -18 to -20 LUFS).  
  - Use audio FX plugins for ambiance, reverb, or equalization.  
- **Tools Needed:** iZotope Ozone (free trial), Adobe Audition's EQ/Compression tools, any royalty-free SFX libraries.  
- **Success Criteria:** Music and effects are clearly audible but not overpowering dialogue (-20 LUFS max).  
- **Common Pitfalls:** Music peaking above -18 LUFS causing clipping.  
- **Time Estimate:** 45 minutes  

**STEP 6: [Mix Balance & EQ]**
- **Action:** Adjust levels for:
  - Dialogue clarity (peak around -3 to -5 LUFS)  
  - Music/ambient tracks (-12 to -16 LUFS)  
  - FX/sfx at a consistent level (-10 to -15 LUFS).  
- **Tools Needed:** iZotope Ozone's Equalizer, Adobe Audition's Metering tools.  
- **Success Criteria:** Balanced mix where no element overpowers others and speech is the dominant focus.  
- **Common Pitfalls:** Overemphasis on music or FX causing loss of dialogue.  
- **Time Estimate:** 60 minutes  

**STEP 7: [Final Mix Review]**
- **Action:** Perform a comprehensive listen-through:
  - Check for any clipping, distortion, or unwanted artifacts.  
  - Ensure consistent volume throughout the episode (no loud spots).  
  - Verify all dialogue edits are smooth and natural-sounding.  
- **Tools Needed:** Headphones with monitoring capabilities, Audacity's peak monitor feature.  
- **Success Criteria:** Clean audio output without any technical issues detected during playback.  
- **Common Pitfalls:** Ignoring final audio peaks or missing hidden artifacts after multiple processing steps.  
- **Time Estimate:** 30 minutes  

**STEP 8: [Mastering Preparation]**
- **Action:** Prepare the file for distribution:
  - Generate a master LRC (lossless) version in WAV/MP3 V0 format.  
  - Create a compressed MP3 at platform-specific bitrate (e.g., 128 kbps for Spotify).  
  - Tag all files with appropriate metadata: title, artist, genre, description, cover art.  
- **Tools Needed:** Hyperscript (free), Adobe Audition's Export Settings, ID3 tag editor like mp3tag (free).  
- **Success Criteria:** All files are correctly tagged and distributed in the correct formats for each platform.  
- **Common Pitfalls:** Incorrect tagging causing errors on platforms, missing metadata fields.  
- **Time Estimate:** 30 minutes  

**STEP 9: [Quality Assurance & Review]**
- **Action:** Conduct a peer review with another producer or editor:
  - Share files for feedback on audio quality and mixing balance.  
  - Incorporate any suggested changes based on reviewer input.  
- **Tools Needed:** Cloud storage (Google Drive, Dropbox), communication tools like Slack or Discord.  
- **Success Criteria:** All issues identified during peer review are addressed before final submission.  
- **Common Pitfalls:** Overlooking minor audio glitches discovered during external review.  
- **Time Estimate:** 15 minutes  

**STEP 10: [Final Distribution & Submission]**
- **Action:** Upload the finalized episode to your hosting platform:
  - Follow all file naming conventions (e.g., YYYY-MM-DD_EPISODE_NUMBER.mp3).  
  - Confirm correct audio tagging and metadata.  
  - Submit for indexing by search engines/platforms.  
- **Tools Needed:** Libsyn, Podbean, or other podcast hosting services, Hyperscript for metadata upload.  
- **Success Criteria:** Episode is live on all platforms with accurate tags and descriptions.  
- **Common Pitfalls:** Incorrect file uploads causing errors in distribution or indexing.  
- **Time Estimate:** 10 minutes  

**STEP 11: [Post-Distribution Monitoring]**
- **Action:** Set up tracking to monitor playback quality:
  - Use hosting platform analytics for downloads, listens, and drop-off points.  
  - Monitor social media mentions and listener feedback on sound quality.  
- **Tools Needed:** Google Analytics for Hosting Service, Twitter/LinkedIn monitoring tools.  
- **Success Criteria:** Positive engagement metrics indicating successful audio delivery.  
- **Common Pitfalls:** Ignoring post-upload analytics leading to undetected distribution issues.  

---

### PHASE 4: OPTIMIZATION & REFINEMENT  

#### Performance Metrics  

1. **Primary Metric:** Audio Quality Score (0-100) based on LUFS levels and noise reduction effectiveness.  
   - Target: ≥90  
   - Measurement Method: Use audio analysis tools to calculate peak levels, noise floor, and distortion metrics.  

2. **Secondary Metrics:**  
   - Mixing Time per Episode: ≤ 2 hours  
   - Audio Edit Fidelity (percentage of edits correctly applied): ≥ 95%  
   - Distribution Success Rate (number of episodes successfully published / total attempts): ≥ 98%  

3. **Long-term Metrics:**  
   - Listener Retention Rate (average episode drop-off point) < 30 seconds  
   - Community Sentiment Score (positive mentions/comments vs. negative) ≥ 80% positive  

#### Iterative Improvement Loop  

1. Measure current performance against targets using the metrics above.  
2. Identify top 3 areas for improvement from listener feedback and analytics.  
3. Implement changes in subsequent episodes: e.g., adjusting compression settings, improving dialogue editing workflow.  
4. Re-measure outcomes to ensure continuous progress toward goals.  

---

### PHASE 5: REPORTING & DOCUMENTATION  

#### Deliverables  

1. **Executive Summary**  
   - Current state vs. target state metrics  
   - Key actions taken for this episode's audio production  
   - Results achieved against defined success criteria  

2. **Detailed Report**  
   - Methodology used (software, plugins, tools)  
   - Research findings and sources cited  
   - Step-by-step execution process with screenshots or logs where applicable  
   - Comparison to previous episodes in terms of quality metrics  

3. **Maintenance Plan**  
   - Ongoing tasks: regular software updates, plugin maintenance, periodic quality audits.  
   - Monitoring schedule: Weekly review of analytics for distribution success and listener feedback.  
   - Update frequency: Monthly check-in on workflow efficiency improvements.  

4. **Knowledge Transfer & Training**  
   - Best practices document shared with team members.  
   - Short training videos demonstrating optimal editing/mixing techniques.  
   - SOPs (Standard Operating Procedures) for future episodes uploaded to a shared drive.  

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE  

#### How to Adapt This Template  

1. **Replace [BRACKETED] Inputs** with actual file names, episode titles, and platform requirements.  
2. **Define 15 Critical Knowledge Areas** based on the latest podcasting trends (e.g., AI-assisted editing, immersive audio formats).  
3. **Map Ultimate Goal to Measurable Outcomes**: Use SMART criteria to define success for each phase.  
4. **Build Step-by-Step Workflow** using proven editing/mixing processes from top podcasts and industry experts.  
5. **Include Latest 2024-2025 Practices**: Integrate AI-powered tools for noise reduction, use of multiband compressors, and dynamic range expansion techniques.

---

### RESEARCH SUB-AGENT CONFIGURATION  

```yaml
research_mission:
  total_agents: 15
  parallel_execution: true
  time_limit: "20 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "AI in Audio Editing"
    focus: "Emerging AI tools for editing and mastering podcasts"
    sources: ["Podcast Engineering forums", "TechCrunch articles"]
    deliverable: "List of top 5 AI-powered audio tools with pricing options"

  # [Continue defining agents 2-15]

consolidation_process:
  1. Collect all agent reports
  2. Prioritize findings by relevance to goals
  3. Create unified action plan from consolidated research  
```  

---

### SUCCESS VALIDATION  

Before marking this template COMPLETE:

- [ ] **Primary Goal Achieved?** Has the podcast episode been edited and mixed to industry standards (LUFS, noise levels) and successfully published across platforms?  
- [ ] **Metrics Met?** Did audio quality metrics exceed 90/100 score? Was distribution success rate ≥98%?  
- [ ] **Quality Validated?** Were all edits verified for accuracy during the final QA step?  
- [ ] **Documentation Complete?** Are all deliverables (report, SOPs) stored in a shared repository with version control?  

---

### TEMPLATE METADATA  

**Last Updated:** 2024-08-08  
**Version:** 1.0  
**Tested With:** Audio Editing workflows for Podcast Production  
**Success Rate:** [To be determined after initial deployment]  
**Average Time to Goal:** [Depends on project complexity, typically 2-3 hours per episode]

*This master template should be copied and customized for each specific podcast production project. The framework remains constant, but the details within each section are profession-specific.*

