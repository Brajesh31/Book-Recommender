# ♿ Accessibility Requirements and Review

## 1. Status

The current templates have basic semantic HTML but no documented accessibility test results. This guide defines the expected review baseline; it is not a claim of WCAG conformance.

## 2. Current template observations

- Both pages declare English as the document language.
- Navigation uses anchor elements.
- The recommendation form has a text input and submit input, but the input currently has no explicit label.
- Book cover images use generic alt text rather than meaningful title-based alternatives.
- Focus styles and keyboard behavior are not explicitly designed.
- No visible validation or no-results feedback is currently implemented.
- The visual design uses dark backgrounds and colored text; actual contrast ratios have not been measured.

## 3. Required improvements

### Navigation and structure
- Use a consistent header and a single clear page-level `h1`.
- Preserve logical heading order.
- Provide a skip link to the main content.
- Use a `main` landmark and meaningful navigation labels.
- Ensure every interactive item works from a keyboard.

### Recommendation form
- Add a visible `label` associated with the input.
- Explain that the app currently expects the exact title present in the model.
- Associate validation text using `aria-describedby`.
- Put the error or result status in a polite live region where appropriate.
- Preserve the entered value after an invalid submission.
- Ensure focus remains predictable after server-rendered errors.

### Book cards and images
- Use descriptive alt text when the image conveys book identity.
- Use empty alt text for purely decorative images.
- Do not encode important details only in the image.
- Keep title and author readable as text.
- Use resilient layout at browser zoom and narrow viewport widths.

### Visual presentation
- Verify text and control contrast against WCAG 2.2 AA criteria.
- Do not use color as the only indicator of state.
- Provide visible focus indicators.
- Respect reduced-motion preferences if animation is introduced.
- Test at 200% zoom and mobile widths.

## 4. Manual keyboard test

1. Load the home page without a mouse.
2. Use Tab and Shift+Tab to traverse all navigation and controls.
3. Confirm visible focus never disappears.
4. Open the recommendation page and reach the input.
5. Submit a valid title using Enter.
6. Submit a blank and unknown title after validation is implemented.
7. Confirm errors are announced and focus is understandable.
8. Confirm all content remains available at 200% zoom.

## 5. Automated and assistive technology checks

When tests are added, include template checks and an accessibility scanner such as axe-core in a browser-based test environment. Automated tools do not replace manual keyboard and screen-reader checks. Record browser, operating system, screen reader, and test date in the accessibility review.

## 6. Release gate

Do not claim accessibility compliance based only on semantic markup or automated scans. Record observed issues, their severity, and any known exceptions before release.
