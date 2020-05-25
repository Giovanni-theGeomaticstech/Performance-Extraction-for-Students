import plotly.express as px
import pandas as pd


#https://plotly.com/python/plotly-express/

def list_creator(Index):
    lists = []
    for value in Index:
        lists.append(value)
    return lists

#Using the histogram to see the distribution of the grades in the class overall
def histo_plotter(plots,bins,type_of_plot,time):
    #num_bins = len(plots)//bins
    print(num_bins)
    if(type_of_plot == "count_people"):
        print("Plot the Number of People per {0} seconds".format(time))
        #print("Generated interval size of {0}".format(bins))
        print("The number of bins being represented: {0}".format(bins))
        
        #Descriptive Statistics
        print("DESCRIPTIVE STATISTICS OF THE PEOPLE COUNT")
        print("Count: ", len(plots)) #for the last element
        #print("Sum: ", np.sum(plots)) #for the last element
        print ("Stdev: ",np.std(plots, dtype=np.float64)) #not sure how accurate as yet
        print(stats.describe(plots))
        df2 = mean(absolute(plots - mean(plots))) 
        print ("Mean absolute deviation: ",df2)
        df3 = median(absolute(plots - median(plots)))
        print ("Median absolute deviation: ",df3)
        
        print("/nHISTOGRAM")
        df = pd.DataFrame({"Count of people": plots})
        fig = px.histogram(df, x="Count of people", nbins=bins)
        fig.update_layout(
        height=600,
        width =800,
        title_text='Count of people in Zone per interval of {0} seconds '.format(time))
        fig.show()
        
        
    elif(type_of_plot == "speed"):
        print("DESCRIPTIVE STATISTICS OF THE SPEEDS")
        print("Plotting the Speed per {0} seconds".format(time))
        print("The number of bins being represented: {0}".format(bins))
        print("Count: ", len(plots)) #for the last element
        #print("Sum: ", np.sum(plots)) #for the last element
        print ("Stdev: ",np.std(plots, dtype=np.float64)) #not sure how accurate as yet
        print(stats.describe(plots))
        df2 = mean(absolute(plots - mean(plots))) 
        print ("Mean absolute deviation: ",df2)
        df3 = median(absolute(plots - median(plots)))
        print ("Median absolute deviation: ",df3)
        
        print("/nHISTOGRAM")
        df = pd.DataFrame({"Speed in Zone": plots})
        fig = px.histogram(df, x="Speed in Zone".format(time), nbins=bins)
        fig.update_layout(
        height=600,
        width =800,
        title_text="Speed per time interval of {0} seconds".format(time))
        fig.show()
   
    #plt.style.use('ggplot')
    #plt.hist(plots, bins = bins) #15 used for all one second intervals
    #plt.hist(plots)
    
    #plt.show()
#https://plot.ly/python/distplot/
def slider_histo(data):
    import plotly.graph_objs as go
    import plotly.figure_factory as ff


#     data  = [30.2049, 51.3693, 51.8094, 30.5573, 56.8151, 45.9166, 56.2858, 55.4125, 72.8778, 
#              39.7996, 34.8203, 36.8362, 39.9959, 54.7995, 52.5158, 40.6841, 61.3939, 48.5818, 
#              41.4944, 71.5607, 49.0913, 57.7985, 70.2787, 45.2226, 55.7449, 69.0475, 33.9624, 
#              51.3384, 53.1948, 46.1682, 66.5202, 37.0265, 48.0182, 44.2164, 56.9336, 69.7961, 
#              48.6728, 44.5923, 33.2164, 41.8337,56.7741, 35.6030, 33.9237, 41.5178, 50.4453, 
#              29.0570, 33.0124, 58.6281, 39.2005, 42.9119]  

    hist_data = [data]
    group_labels = ['distplot']
    f = ff.create_distplot(hist_data, group_labels, bin_size=1, show_rug=True,show_curve=False)
    fig = go.FigureWidget(f)
    fig.data[0].marker.line =  dict( color = 'black',width = 2)
    fig.data[1].line.color = 'red'
    fig.layout.sliders = [dict(
                    active = 0,
                    currentvalue = {"prefix": "bin size: "},
                    pad = {"t": 20},
                    steps = [dict(label = i, method = 'restyle',  args = ['xbins.size', i]) for i in range(1,100)]
                )]
    fig.show()
###############################################################################################
#The function scatter_plotter consumer the parameters plots1 which is an array of the values that would be used for the x values of the dataset.
#The array plots 2 which is used for the y values. A string type of plot which determines whether if it is a
#speed calculation and lastly time which is an integer corresponding to the interval time.
###############################################################################################
#The modifications made is an output of a scatterplot.
###############################################################################################
   
#scatter_plotter: (Array of Float) Int Str Int -> None
###############################################################################################

#Scatter plot to see the distribution of an individuals grade 
def scatter_plotter(df,type_plot,section,ID):
    print(df)
    #print(df.columns)
    #Getting all the ID's
    #original = df[df['ID'] == 0] #Original values  row    
    #student = df[df['ID'] == 100000].values #Student values  row
    original = list(df.loc[0]) #Original values  row
    student = list(df.loc[1]) #Student values  
    
    temp = list_creator(df.columns) #getting columns in a more useable format
    length = len(temp)
    plots_x = (temp[1:length]) * 2 # * by the number multiplier
    print(plots_x)

    plot_sec = ["Student"] * (length - 1)
    plot_sec.extend(["Original"] * (length - 1))
    print(plot_sec)

    #plots_y = original[1][1:length] + student[1][1:length]
    plots_y = student[1:len(student)] + original[1:len(original)]  #

    #list(original.iloc[0]) #iloc is for integer based selection can also select columns [row,column]
    # loc is used too by row index selection

    print(plots_y)
    
    
    if(type_plot == "stud"):#If the type of plot is just a student 
        #Section shows whether it is knowledge, communication, or so on
        #Note I should have to worry about making this section again
        #Just need the dataframe information
        #X would be the section to show the marks by
        #Y would be the section for the students
        df = pd.DataFrame({"Grade Categories": plots_x,"Score":plots_y, "Type":plot_sec})
        fig = px.line(df,x="Grade Categories",y = "Score", color="Type")
        fig.data[0].update(mode = 'markers+lines') #getting scatter matter lines
        fig.update_layout(
        height=600,
        width =800,
        title_text='{1} - {0} Mark Distribution'.format(section,ID))

        fig.show()
    


def line_plotter(plots1,plots2,type_plot,time):
    
    if(type_plot == "count_speed"):
        #Plotting the data on the graph moving away from zone
        plt.scatter(plots1,plots2,color='blue', label = "Speed against People in Zone") #Need to make a proper axis
        #naming the x axis
        plt.xlabel('Count of People in Zone')
        #naming the y-axis
        plt.ylabel('Calculated speed per {0}'.format(time))
        plt.title("Speeds vs People in Zone")
    plt.show()
