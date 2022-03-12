#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
require(readr)
library(ggplot2)
library(dplyr)

nba <- read_csv('data/nba.csv')

shinyServer(function(input, output) {

    output$distPlot <- renderPlot({
        ggplot(nba, aes(x = input$xcol, y = reorder(name, input$xcol))) +
          geom_bar(stat="identity")
    })
    
    output$bar <- renderPlot({
      ggplot(nba, aes(x = pts, y = reorder(name, pts))) +
        geom_bar(stat="identity") +
        xlab("Average Points per Game") + 
        ylab("Player")
    })
 
    output$scatter <- renderPlot({
      ggplot(nba, aes(x=min, y=pts)) +
        geom_point() +
        geom_text(aes(label = name), check_overlap = TRUE) +
        xlab("Average Minutes Played per Game") +
        ylab("Average Points per Game")
    })
    
    output$table <- DT::renderDataTable(DT::datatable({
      nba
    }))
    
    output$age <- renderPlot({
      ggplot(data=nba, aes(age)) +
        geom_histogram(binwidth = input$bin)
      # freqpoly(rnorm(nba$age), binwidth=input$bin)
    })

    # output$glossary <- renderPrint({
    #   "index name team age gp: games played w:wins l: losses min:average minutes played per game pts: points fgm: fga fgp threepm threepa threepp ftm fta ftp oreb dreb reb ast tov stl blk pf fp dd2 td3 plusminus"
    # })

})
