using MongoDB.Driver;
using Microsoft.EntityFrameworkCore;
using Hangman;
using Hangman.Services;

//var connectionString = "mongodb+srv://games-dev:exK0juZnNZJzaJQK@west-cluster.p2tfglm.mongodb.net/?retryWrites=true&w=majority";
//if (connectionString == null)
//{
//    Environment.Exit(0);
//}

//var client = new MongoClient(connectionString);
//var dbContextOptions =
//    new DbContextOptionsBuilder<GamesDbContext>().UseMongoDB(client, "games");
//var db = new GamesDbContext(dbContextOptions.Options);

var builder = WebApplication.CreateBuilder(args);


//builder.Services.AddTransient<IWordService, WordService>();

builder.Services.AddRazorPages();
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddDependencyInjection();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
