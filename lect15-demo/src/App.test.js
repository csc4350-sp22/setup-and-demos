import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

test('renders header sentence', () => {
  render(<App />);
  const linkElement = screen.getByText("Bands I am seeing Friday");
  expect(linkElement).toBeInTheDocument();
});

test('text field added to doc on button click', () => {
  render(<App />);
  const buttonElement = screen.getByText("Click me!");
  expect(buttonElement).toBeInTheDocument();

  const inputElement = screen.getByTestId("input-field");
  expect(inputElement).toBeInTheDocument();

  fireEvent.change(inputElement, {"target": {"value": "My Chemical Romance"}});
  fireEvent.click(buttonElement);

  const newBandElement = screen.getByText("My Chemical Romance");
  expect(newBandElement).toBeInTheDocument();

});
