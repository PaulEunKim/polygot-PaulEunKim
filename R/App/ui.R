#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(

  navbarPage(
    "NBA Statistics Exploration",
    
    tabPanel("Bar Graphs",
                   tabsetPanel(type = "tabs",
                               
                               tabPanel("Points", plotOutput("bar")),
                               tabPanel("Points Per Minute", plotOutput("scatter")),
                   )
                   
             ),
    
    tabPanel("Data", 
             DT::dataTableOutput("table")),
  
    tabPanel("Distribution of Age",
             fluidRow(
               column(3, wellPanel(
                 sliderInput("bin", "Binwidth:", min = 0, max = 5, value = .5,
                             step = .1),
                 submitButton("Submit")
               )),
               column(6,
                      plotOutput("age"),
               )
             )
             )
    
    
    
  )
  
  
))
