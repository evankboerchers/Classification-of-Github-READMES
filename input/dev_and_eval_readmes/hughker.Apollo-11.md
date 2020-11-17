Apollo-11
=========

Original Apollo 11 guidance computer (AGC) source code, converted from their custom .agc files to .s files for syntax highlighting, for Command Module (Comanche055) and Lunar Module (Luminary099). Digitized by the folks at [Virtual AGC](http://www.ibiblio.org/apollo/) and [MIT Museum](http://web.mit.edu/museum/). The goal is to be a repo for the original Apollo 11 source code. As such, PRs are welcome for any issues identified between the transcriptions in this repository and the original source scans for [Luminary 099](http://www.ibiblio.org/apollo/ScansForConversion/Luminary099/) and [Comanche 055](http://www.ibiblio.org/apollo/ScansForConversion/Comanche055/), as well as any files I may have missed.
##Compilation
If you are interested in compiling the original source code, check out [Virtual AGC](https://github.com/rburkey2005/virtualagc).

##Attribution

     Copyright: Public domain.
     Filename:  CONTRACT_AND_APPROVALS.agc
     Purpose:   Part of the source code for Colossus 2A, AKA Comanche 055.
                It is part of the source code for the Command Module's (CM)
                Apollo Guidance Computer (AGC), for Apollo 11.
     Assembler: yaYUL
     Contact:   Ron Burkey <info@sandroid.org>.
     Website:   www.ibiblio.org/apollo.
     Mod history:   2009-05-06 RSB  Transcribed from page images.

     This source code has been transcribed or otherwise adapted from digitized
     images of a hardcopy from the MIT Museum.  The digitization was performed
     by Paul Fjeld, and arranged for by Deborah Douglas of the Museum.  Many
     thanks to both.  The images (with suitable reduction in storage size and
     consequent reduction in image quality as well) are available online at
     www.ibiblio.org/apollo.  If for some reason you find that the images are
     illegible, contact me at info@sandroid.org about getting access to the
     (much) higher-quality images which Paul actually created.

     Notations on the hardcopy document read, in part:

        Assemble revision 055 of AGC program Comanche by NASA
        2021113-051.  10:28 APR. 1, 1969  

     Page 1

    #************************************************************************
    #                                                                       *
    #       THIS AGC PROGRAM SHALL ALSO BE REFERRED TO AS:                  *
    #                                                                       *
    #                                                                       *
    #               COLOSSUS 2A                                             *
    #                                                                       *
    #                                                                       *
    #   THIS PROGRAM IS INTENDED FOR USE IN THE CM AS SPECIFIED             *
    #   IN REPORT R-577.  THIS PROGRAM WAS PREPARED UNDER DSR               *
    #   PROJECT 55-23870, SPONSORED BY THE MANNED SPACECRAFT                *
    #   CENTER OF THE NATIONAL AERONAUTICS AND SPACE                        *
    #   ADMINISTRATION THROUGH CONTRACT NAS 9-4065 WITH THE                 *
    #   INSTRUMENTATION LABORATORY, MASSACHUSETTS INSTITUTE OF              *
    #   TECHNOLOGY, CAMBRIDGE, MASS.                                        *
    #                                                                       *
    #************************************************************************


    SUBMITTED:  MARGARET H. HAMILTON        DATE:   28 MAR 69
        M.H.HAMILTON, COLOSSUS PROGRAMMING LEADER
        APOLLO GUIDANCE AND NAVIGATION

    APPROVED:   DANIEL J. LICKLY        DATE:   28 MAR 69
        D.J.LICKLY, DIRECTOR, MISSION PROGRAM DEVELOPMENT
        APOLLO GUIDANCE AND NAVIGATION PROGRAM

    APPROVED:   FRED H. MARTIN          DATE:   28 MAR 69
        FRED H. MARTIN, COLOSSUS PROJECT MANAGER
        APOLLO GUIDANCE AND NAVIGATION PROGRAM

    APPROVED:   NORMAN E. SEARS         DATE:   28 MAR 69
        N.E. SEARS, DIRECTOR, MISSION DEVELOPMENT
        APOLLO GUIDANCE AND NAVIGATION PROGRAM

    APPROVED:   RICHARD H. BATTIN       DATE:   28 MAR 69
        R.H. BATTIN, DIRECTOR, MISSION DEVELOPMENT
        APOLLO GUIDANCE AND NAVIGATION PROGRAM

    APPROVED:   DAVID G. HOAG           DATE:   28 MAR 69
        D.G. HOAG, DIRECTOR
        APOLLO GUIDANCE AND NAVIGATION PROGRAM

    APPROVED:   RALPH R. RAGAN          DATE:   28 MAR 69
        R.R. RAGAN, DEPUTY DIRECTOR
        INSTRUMENTATION LABORATORY
