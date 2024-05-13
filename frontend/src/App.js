import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
/*
import About from './components/About';
import Contact from './components/Contact';
import NotFound from './components/NotFound';
*/

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={Dashboard} />
          <Route component={NotFound} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
