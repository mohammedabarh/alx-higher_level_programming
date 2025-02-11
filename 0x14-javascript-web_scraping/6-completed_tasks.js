#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = todos.filter(todo => todo.completed);
    const tasksByUser = completedTasks.reduce((acc, todo) => {
      acc[todo.userId] = (acc[todo.userId] || 0) + 1;
      return acc;
    }, {});
    console.log(tasksByUser);
  }
});
