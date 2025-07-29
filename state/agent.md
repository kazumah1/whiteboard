# AI Code Assistant Guide (agents.md)

This document provides comprehensive guidelines for AI-assisted development to ensure high-quality, maintainable, and scalable code output.

## Core Principles

### 1. Code Quality First
- **Readability**: Code should be self-documenting and easy to understand
- **Consistency**: Follow established patterns and conventions throughout the project
- **Simplicity**: Prefer simple, clear solutions over complex ones
- **Maintainability**: Write code that can be easily modified and extended

### 2. Iterative Development
- Start with working, simple implementations
- Refactor incrementally for better design
- Test each iteration thoroughly
- Document decisions and trade-offs

## Code Style Guidelines

### General Style Rules
1. **Naming Conventions**
   - Use descriptive, meaningful names for variables, functions, and classes
   - Follow language-specific conventions (camelCase, snake_case, PascalCase)
   - Avoid abbreviations and single-letter variables (except loop counters)
   - Use verbs for functions, nouns for variables/classes

2. **Function Design**
   - Keep functions small and focused (single responsibility)
   - Limit parameters (max 3-4, use objects/structs for more)
   - Return early when possible to reduce nesting
   - Use pure functions when feasible

3. **Error Handling**
   - Handle errors explicitly, don't ignore them
   - Use appropriate error types for the language
   - Provide meaningful error messages
   - Fail fast and fail clearly

### Language-Specific Guidelines

#### JavaScript/TypeScript
```javascript
// Good: Descriptive naming and clear structure
const calculateTotalPrice = (items, taxRate) => {
  if (!items || items.length === 0) {
    return 0;
  }
  
  const subtotal = items.reduce((sum, item) => sum + item.price, 0);
  return subtotal * (1 + taxRate);
};

// Use TypeScript for better type safety
interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
}
```

#### Python
```python
# Good: Clear function with type hints
def process_user_data(
    users: List[Dict[str, Any]], 
    filter_active: bool = True
) -> List[User]:
    """Process user data and return filtered User objects."""
    processed_users = []
    
    for user_data in users:
        if filter_active and not user_data.get('is_active', False):
            continue
            
        user = User.from_dict(user_data)
        processed_users.append(user)
    
    return processed_users
```

## Testing Strategy

### 1. Test-Driven Development (TDD)
- Write tests before implementing features
- Follow Red-Green-Refactor cycle
- Start with simple test cases, then add edge cases

### 2. Test Structure
```javascript
// Example test structure
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid data', () => {
      // Arrange
      const userData = { name: 'John', email: 'john@example.com' };
      
      // Act
      const result = userService.createUser(userData);
      
      // Assert
      expect(result).toBeDefined();
      expect(result.id).toBeTruthy();
    });
    
    it('should throw error for invalid email', () => {
      // Test edge cases and error conditions
      const invalidData = { name: 'John', email: 'invalid-email' };
      
      expect(() => userService.createUser(invalidData))
        .toThrow('Invalid email format');
    });
  });
});
```

### 3. Test Coverage Goals
- **Unit Tests**: Test individual functions/methods (aim for 80%+ coverage)
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete user workflows
- **Edge Cases**: Test boundary conditions and error scenarios

## Code Review Guidelines

### Self-Review Checklist
Before submitting code, verify:

1. **Functionality**
   - [ ] Code works as intended
   - [ ] Edge cases are handled
   - [ ] Error conditions are managed properly

2. **Quality**
   - [ ] Code follows style guidelines
   - [ ] Functions are small and focused
   - [ ] Names are descriptive and consistent
   - [ ] No commented-out code or debug statements

3. **Performance**
   - [ ] No obvious performance issues
   - [ ] Efficient algorithms and data structures
   - [ ] Proper resource management (memory, connections)

4. **Security**
   - [ ] Input validation is implemented
   - [ ] No hardcoded secrets or sensitive data
   - [ ] Proper authentication/authorization checks

5. **Documentation**
   - [ ] Complex logic is commented
   - [ ] Public APIs are documented
   - [ ] README is updated if needed

## Iteration Techniques

### 1. Incremental Development
```
Phase 1: Core functionality (minimal viable implementation)
Phase 2: Add edge case handling
Phase 3: Optimize performance
Phase 4: Add advanced features
Phase 5: Refactor for maintainability
```

### 2. Refactoring Approach
- **Extract Methods**: Break down large functions
- **Extract Constants**: Replace magic numbers/strings
- **Eliminate Duplication**: Use DRY principle
- **Improve Naming**: Make intent clearer
- **Simplify Conditionals**: Reduce complexity

### 3. Performance Optimization
- Measure before optimizing
- Focus on bottlenecks, not micro-optimizations
- Consider algorithmic improvements first
- Use profiling tools to identify issues

## Best Practices by Domain

### Frontend Development
- **Component Design**: Small, reusable components
- **State Management**: Minimize shared state, use proper state management patterns
- **Accessibility**: Follow WCAG guidelines
- **Performance**: Optimize bundle size, lazy loading

### Backend Development
- **API Design**: RESTful principles, consistent naming
- **Database**: Proper indexing, query optimization
- **Security**: Input validation, authentication, authorization
- **Monitoring**: Logging, metrics, health checks

### DevOps/Infrastructure
- **Configuration**: Environment-specific configs
- **Deployment**: Automated, repeatable processes
- **Monitoring**: Comprehensive logging and alerting
- **Scaling**: Design for horizontal scaling

## Common Anti-Patterns to Avoid

### Code Smells
- **God Classes**: Classes that do too much
- **Long Methods**: Functions over 20-30 lines
- **Deep Nesting**: More than 3 levels of indentation
- **Magic Numbers**: Unexplained constants
- **Duplicate Code**: Copy-paste programming

### Design Issues
- **Tight Coupling**: Components too dependent on each other
- **Circular Dependencies**: Modules importing each other
- **Premature Optimization**: Optimizing before measuring
- **Over-Engineering**: Adding unnecessary complexity

## Documentation Standards

### Code Comments
```javascript
/**
 * Calculates the optimal route between two points
 * @param {Point} start - Starting coordinates
 * @param {Point} end - Destination coordinates
 * @param {RouteOptions} options - Route calculation options
 * @returns {Promise<Route>} Optimized route with waypoints
 */
async function calculateRoute(start, end, options = {}) {
  // Implementation details...
}
```

### README Structure
```markdown
# Project Name

## Description
Brief description of what the project does

## Installation
Step-by-step installation instructions

## Usage
Basic usage examples

## API Documentation
If applicable, API endpoints and usage

## Contributing
Guidelines for contributors

## License
License information
```

## Debugging and Troubleshooting

### Debugging Strategy
1. **Reproduce the Issue**: Create minimal test case
2. **Isolate the Problem**: Use debugging tools, add logging
3. **Form Hypotheses**: Based on symptoms and code analysis
4. **Test Systematically**: Verify or disprove each hypothesis
5. **Fix and Verify**: Implement fix and ensure it works

### Logging Best Practices
```javascript
// Good logging with context
logger.info('User authentication successful', {
  userId: user.id,
  sessionId: session.id,
  timestamp: new Date().toISOString()
});

// Structured error logging
logger.error('Database connection failed', {
  error: error.message,
  stack: error.stack,
  connectionString: sanitizedConnectionString
});
```

## Security Considerations

### Input Validation
- Validate all user inputs
- Use whitelisting over blacklisting
- Sanitize data before processing
- Use parameterized queries for databases

### Authentication & Authorization
- Implement proper session management
- Use secure password hashing
- Implement rate limiting
- Follow principle of least privilege

## Performance Guidelines

### Optimization Priorities
1. **Algorithmic Efficiency**: Choose right algorithms and data structures
2. **Database Optimization**: Proper indexing, query optimization
3. **Caching Strategy**: Implement appropriate caching levels
4. **Resource Management**: Proper cleanup, connection pooling

### Monitoring Metrics
- Response times
- Error rates
- Resource utilization
- User experience metrics

## Conclusion

Following these guidelines will result in code that is:
- **Readable**: Easy to understand and maintain
- **Reliable**: Well-tested and robust
- **Scalable**: Can handle growth and change
- **Secure**: Protects against common vulnerabilities
- **Performant**: Efficient and responsive

Remember: The goal is not perfect code, but code that effectively solves problems while being maintainable and reliable. Always consider the trade-offs between different approaches and choose the solution that best fits the project's needs and constraints.