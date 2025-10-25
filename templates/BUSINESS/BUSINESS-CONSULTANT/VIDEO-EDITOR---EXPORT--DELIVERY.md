# Video Editor - AI Agent Template
## Export & Delivery

### Success Definition (Measurable)
- **Final Export File:** 1080p H.264 MP4 or ProRes 4K with embedded metadata
- **Delivery Format Verification:** [✓] All files meet industry-standard specifications (e.g., ISO 2309:2011 for container formats, ITU-R BT.1886 for color standards)
- **Quality Assurance:** Passes frame-by-frame visual inspection and bitrate validation without errors
- **Timeline Adherence:** Delivered within the agreed-upon deadline with no critical milestones missed
- **Accessibility Verification:** [✓] Export includes closed captions (SRT) and audio descriptions if applicable

### Critical Knowledge Areas for Video Editor

1. **Editing Techniques** - Color grading, B-Roll integration, Storyboarding workflow
2. **Software Proficiency** - NLE capabilities of Premiere Pro/FCP vs DaVinci Resolve
3. **Audio Post-Production** - Synchronization, noise reduction, ADR implementation
4. **Color Correction & Grading** - LUT application, Primary/Secondary corrections
5. **Motion Graphics** - Animation principles in After Effects or Blender
6. **Export Settings Optimization** - Bitrate balancing vs file size trade-offs
7. **Project Management** - Timeline structuring for multi-editor workflows
8. **Collaboration Tools** - Cloud storage best practices (Google Drive, Dropbox)
9. **Regulatory Compliance** - Copyright considerations for assets used
10. **Automation & Scripting** - Using Python/Node.js to batch process exports
11. **Backup Strategies** - RAID vs cloud redundancy approaches
12. **Timeline Compression Techniques** - Removing unused footage without re-encoding

### Execution Workflow Steps

**STEP 1: Project Setup**
- **Action:** Create new project folder structure (raw, edit, output)
- **Tools:** Adobe Creative Cloud/Resolve Studio, Google Drive/Dropbox
- **Success Criteria:** Folder exists with appropriate subfolders for raw media, edited sequence, final exports
- **Common Issues:** Overwriting files without version control
- **Time Estimate:** 15 minutes

**STEP 2: Media Import & Organization**
- **Action:** Drag all source clips into project timeline, group by scene or event
- **Tools:** Adobe Premiere Pro/Resolve, DaVinci Rename (free)
- **Success Criteria:** All media imported with metadata intact, no missing files
- **Common Issues:** Large AVI files not importing correctly due to codec issues
- **Time Estimate:** 30 minutes

**STEP 3: Rough Edit Assembly**
- **Action:** Create rough cut by moving clips into logical order, add markers for key moments
- **Tools:** Premiere Pro Timeline, Resolve Fusion Editor
- **Success Criteria:** Rough edit is coherent with minimal cuts, all source files are accounted for
- **Common Issues:** Out-of-sync audio due to frame drift
- **Time Estimate:** 45 minutes

**STEP 4: Fine Cut & Polish**
- **Action:** Refine pacing, add transitions, apply color correction across entire cut
- **Tools:** DaVinci Resolve Color Editor, Premiere Pro Effects Panel
- **Success Criteria:** Edit is smooth with consistent timing and visual style
- **Common Issues:** Over-application of LUT causing unwanted hue shifts
- **Time Estimate:** 2 hours

**STEP 5: Audio Mix**
- **Action:** Sync audio tracks, adjust levels, add effects like EQ or de-esser
- **Tools:** Adobe Audition/AudioSuite in Premiere Pro
- **Success Criteria:** All dialogues are clear, music matches energy level without distortion
- **Common Issues:** Crossfades cause popping artifacts when too sharp
- **Time Estimate:** 1 hour

**STEP 6: Final Review & Cleanup**
- **Action:** Run through entire edit to check for continuity errors or missing frames
- **Tools:** Playback in full resolution, built-in inspector panel
- **Success Criteria:** No dropped frames, all scenes are properly rendered with no artifacts
- **Common Issues:** Outliers like test footage or placeholder clips remaining in final export
- **Time Estimate:** 30 minutes

**STEP 7: Export Settings Configuration**
- **Action:** Select output format (e.g., H.264 MP4 for web), configure bitrate, codec options
- **Tools:** Adobe Media Encoder, Resolve Rendering Queue
- **Success Criteria:** Output settings match target delivery platform specifications
- **Common Issues:** Choosing incorrect preset leading to larger-than-needed files
- **Time Estimate:** 15 minutes

**STEP 8: Batch Export**
- **Action:** Use media encoder or batch rendering to process all sequences into final format
- **Tools:** Adobe Media Encoder Queue, Resolve Output Queue
- **Success Criteria:** All exports complete without errors, output folder organized
- **Common Issues:** Hardware encoding issues on low-spec machines causing failures
- **Time Estimate:** Varies based on project size

**STEP 9: Quality Assurance Verification**
- **Action:** Perform frame-by-frame inspection of first and last 10 seconds, check file metadata
- **Tools:** VLC Media Player, FFProbe for metadata validation
- **Success Criteria:** No playback issues, correct aspect ratio, embedded subtitles/audio tracks
- **Common Issues:** Exporting in wrong resolution or missing audio track
- **Time Estimate:** 15 minutes

**STEP 10: Delivery Preparation**
- **Action:** Compress final files if needed (e.g., for email), create folder structure with metadata
- **Tools:** 7-Zip, Adobe Bridge
- **Success Criteria:** Files are ready for distribution without extra instructions
- **Common Issues:** Large individual file sizes making them impractical to send
- **Time Estimate:** 10 minutes

**STEP 11: Final Handoff & Documentation**
- **Action:** Package final files with accompanying PDF containing project notes and version history
- **Tools:** ZIP utility, Google Docs/Confluence
- **Success Criteria:** All deliverables are received by client/stakeholder with no missing components
- **Common Issues:** Files not backed up properly before handoff
- **Time Estimate:** 15 minutes

### Tools & Software Stack (Primary Free/Open Source)

**Essential Tools:**
1. **Editing Platform:** DaVinci Resolve (Free, Recommended)
2. **Project Management:** Google Drive/OneDrive (Cloud Sync) or Dropbox Business
3. **Version Control:** Git for collaborative projects on shared assets
4. **Color Correction:** DaVinci Resolve Color Panel (Free)
5. **Audio Post-Prod:** Adobe Audition/AudioSuite in Premiere Pro
6. **Export Pipeline:** Adobe Media Encoder (built into Resolve) or FFmpeg CLI
7. **Collaboration:** Slack/Teams for real-time communication
8. **Backup Solutions:** Google Drive 2GB free tier + On-Premise RAID Storage
9. **Scripting/Automation:** Python with ffmpeg module, Node.js for batch workflows

**Optional Paid Alternatives:**
1. **Editing Platform:** Adobe Premiere Pro (Subscription) - $20/month per user
2. **Audio Post-Prod:** Avid Media Composer (License-based)
3. **Color Correction UI Enhancements:** Resolve FX 360 ($299/year)
4. **Export Acceleration:** HandBrake Pro ($299/year) for hardware encoding
5. **Collaboration:** Perforce Helix Core (Teamwork licensing)

### Troubleshooting Common Issues

**1. File Import Failures**
- Check file codecs are supported by the NLE
- Ensure no ransomware/malware protection blocks access during import
- Try renaming files to remove special characters

**2. Playback Jank or Dropped Frames**
- Verify source media is not corrupted
- Lower resolution preview settings for faster iteration
- Check hardware encoding capabilities (GPU acceleration)

**3. Color Grading Issues**
- Always start with a color reference frame (e.g., LUT)
- Use 16-bit depth for intermediate renders to prevent banding
- Profile footage to match intended delivery space

**4. Audio Sync Problems**
- Manually sync audio levels rather than relying on automatic timecode matching
- Add small fade-ins/out to avoid popping artifacts at transitions
- Export with a temporary naming convention for easy identification (e.g., "Cut_01_ColorCorrected")

**5. Large File Size Concerns**
- Use hardware encoding when possible (GPU acceleration)
- Split export into smaller batches if processing takes too long
- Compress files post-export using tools like VLC or HandBrake

### Recommended Tool Stack for 2024-2025 Video Editing

| Category | Primary Tools (Free/Open Source) | Premium Alternatives |
|----------|----------------------------------|-----------------------|
| Editing Platform | DaVinci Resolve (Free, Full Feature NLE) | Adobe Premiere Pro (Subscription), Avid Media Composer (License-based) |
| Audio Post-Prod | Adobe Audition/AudioSuite in NLEs | Pro Tools (Avid), Logic Pro X |
| Export Pipeline | Adobe Media Encoder (built into Resolve) or FFmpeg CLI | HandBrake Pro, Warp Studio (Paid Plugin for Premiere) |
| Collaboration | Google Drive/Dropbox Business | Perforce Helix Core (Enterprise Licensing) |
| Version Control & Backup | Git (Integrates with cloud services) | SVN (Subversion) for larger teams |
| Scripting/Automation | Python + ffmpeg module, Node.js | Ruby with FFmpeg bindings |

### Realistic Timeline to Achieve Export & Delivery

**Week 1: Project Setup and Initial Import**
- Days 1-2: Folder structure creation
- Days 3-4: Media ingestion and initial organization

**Week 2: Rough Edit & First Review Cycle**
- Days 5-7: Rough assembly and preliminary cuts
- Day 8: Internal review with feedback integration

**Week 3: Fine Cut & Audio Mix**
- Days 9-12: Finalizing edit, polishing transitions
- Day 13: Sound design and mixing session

**Week 4: Final Polish & Export Prep**
- Days 14-16: Color correction/grading and final review
- Day 17: Export settings configuration and initial test renders
- Day 18: Full batch export of all sequences
- Day 19: Quality assurance checks on selected samples
- **Buffer Day:** Day 20 for unexpected issues or client feedback

**Week 5: Delivery & Handoff**
- Day 21: Final packaging, documentation creation
- Day 22: Client review and sign-off
- Day 23: Secure delivery via cloud storage with access instructions
- **Follow-Up:** Schedule a brief call to confirm successful playback on intended devices

